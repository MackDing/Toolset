#!/bin/bash

# 需提前准备vas流媒体包解压到主节点/data/ev-box/storage/

# 定义变量
storage_dir="/data/ev-box/storage"
target_dir="/home/mack"
host_ip="192.168.1.141" 
node_ip="172.16.150.13"
username="admin"
pwd="admin"
new_sdk="cvmart-zhuhai-tcr.tencentcloudcr.com/public_images/duliao13631bmtpu11004:202306271405"
aid="11004"
new_http_port="12580"
zh_name="堵料识别"
algo_info='    - {"name":"'"$zh_name"'","id":'"$aid"',"port":'"$new_http_port"',"ip":"'"$node_ip"'","roi":[{"type": "polygon","key": "polygon_1"},{"type": "line","key": "line_1"}],"thresh-name":"conf_thresh","thresh": 0.5,"interval": 1000,"qps":16,"cover":"/storage/10850.png","color":"#D5C20D"}'
# [demo注意缩进] new_info='      - {"name": "安全帽识别", "id": 9510, "port": 14611, "ip": "172.16.140.11", "roi": [{"type": "polygon", "key": "polygon_1"}], "thresh-name": "conf_thresh", "thresh": 0.5, "interval": 1000, "qps": 16, "cover": "/storage/10850.png", "color": "#D5C20D"}'

# 检查目录是否存在
if [ -d "$target_dir" ]; then
  echo "目录已存在: $target_dir"
else
  # 创建目录
  sudo mkdir -p "$target_dir"
  echo "已创建目录: $target_dir"
fi

# 到子节点挂载
sshpass -p "'"$username"'" ssh $username@$node_ip&&

if [ -d "$storage_dir" ]; then
  echo "目录已存在: $storage_dir"
else
  # 创建目录
  sudo mkdir -p "$storage_dir"
  echo "已创建目录: $storage_dir"
fi
# 检查挂载点是否已经挂载
if grep -qs "$storage_dir" /proc/mounts; then
  echo "目录已挂载: $storage_dir"
else
  # 挂载目录
  sudo mount -t nfs -o nolock "$host_ip:/data/ev-box/storage" "$storage_dir"
  echo "已挂载目录: $storage_dir"
fi
echo -e "`df -h`\n"
# 定义变量
rc_local_file="/etc/rc.local"
mount_command="mount -t nfs -o nolock \"$host_ip\":/data/ev-box/storage /data/ev-box/storage"
check_command="grep -qxF \"$mount_command\" \"$rc_local_file\""

# 检查是否已经存在挂载指令
if eval "$check_command"; then
  echo "挂载指令已存在于 $rc_local_file"
else
  # 添加挂载指令到 rc.local 文件末尾
  echo "$mount_command" >> "$rc_local_file"
  echo "已将挂载指令添加到 $rc_local_file"
fi

# 定义变量
container_name="$aid"
container_image="$new_sdk"

# 检查是否存在相同容器名的容器
if docker ps -a --format "{{.Names}}" | grep -q "^$container_name$"; then
  # 删除已存在的容器
  docker rm -f "$container_name"
  echo "已删除已存在的容器: $container_name"
fi

# 生成容器
docker create -it --net host --name "$container_name" --privileged --restart=unless-stopped --log-driver=none --device=/dev/bm-tach-0 --device=/dev/bm-tach-1 --device=/dev/bm-top --device=/dev/bm-tpu0 --device=/dev/bm-vpp --device=/dev/bm-wdt-0 --device=/dev/bm_efuse --device=/dev/bmdev-ctl -v /data/ev-box/storage/"$container_name":/usr/local/vas -v /etc/localtime:/etc/localtime -v /data/ev-box/storage/tmp:/usr/local/vas/tmp -v /data/smc:/data/smc  -e PATH=\$PATH:/opt/sophon/sophon-ffmpeg_0.5.1/bin/ "$container_image"
echo "已生成容器: $container_name"

# 启动容器
docker start "$container_name"
echo "已启动容器: $container_name"

# 退出子节点
exit

cp -r /data/ev-box/storage/vas /data/ev-box/storage/'"$aid"'

# 配置修改
sed -i "s/^aid=.*/aid=$aid/" /data/ev-box/storage/"$aid"/local.conf
sed -i "s/^http_port=.*/http_port=$new_http_port/" /data/ev-box/storage/"$aid"/local.conf
sed -i "s/^ip=.*/ip=$host_ip/" /data/ev-box/storage/"$aid"/local.conf

sed -i "s/\(\"call_back\": \"http:\/\/\)[^:]*\(:[0-9]\{1,\}\/api\/open\/callback\/handle\"\)/\1$new_ip\2/" /data/ev-box/storage/"$aid"/run.conf

yml_file="application-test1.yml"
# 检查algo_info是否存在于yml文件的info部分
if ! grep -q "$algo_info" "$yml_file"; then
  # 将algo_info插入到yml文件的info部分
  sed -i '/^info:/a\'$'\n'"$algo_info" "$yml_file"
  echo "algo_info inserted into info"
else
  echo "algo_info already exists in info"
fi


# 中心授权
cd "$target_dir"

# 检查是否成功进入目录
if [ "$(pwd)" == "$target_dir" ]; then
  echo "成功进入目录: $target_dir"
else
  echo "无法进入目录: $target_dir"
fi
# 检查 jq 是否已安装
if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Installing..."
    apt install jq -y
else
    echo "jq is already installed."
fi

# 登录获取 access_token
login_response=$(wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header 'Content-Type: text/plain' \
  --header 'Cookie: JSESSIONID=405E1E4E7858F3C55684BF36D83FE67E' \
  --body-data '{"username":"admin","password":"test2021","type":"1","rememberMe":"true"}' \
   'http://192.168.1.138/ev-amp-user/api/auth/login')

sleep 1
login_response=$(cat login)
access_token=$(echo "$login_response" | jq -r '.data.access_token')
echo "access_token: $access_token"

# 新增算法
wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header "Token: $access_token" \
  --header 'Content-Type: application/json' \
  --header 'Cookie: JSESSIONID=67447F58775D508042D0BE82CA533558' \
  --body-data "{\"saleType\":\"non-repurchase\",\"id\":$aid,\"name\":\"$zh_name\",\"nameEn\":$aid,\"type\":\"video\",\"analysisRequires\":[9],\"cover\":\"\",\"audio\":\"\"}" \
   'http://192.168.1.138/ev-amp-store/api/algo/save/nonRepurchase'

# 临时授权
wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header 'Content-Type: application/json' \
  --header "Token: $access_token" \
  --header 'Cookie: JSESSIONID=405E1E4E7858F3C55684BF36D83FE67E' \
  --body-data "{\"authType\":2,\"authDays\":90,\"pattern\":1,\"payload\":253,\"algoDetailList\":[{\"algoId\":$aid,\"waysNum\":11,\"qpsNum\":0,\"authModel\":\"ways\",\"type\":\"video\",\"algoName\":\"$zh_name\"}]}" \
   'http://192.168.1.138/ev-amp-store/api/ev/auth/add'

# 下载授权文件并保存为ev-box.lic
wget --no-check-certificate --quiet \
  --header 'Cookie: JSESSIONID=405E1E4E7858F3C55684BF36D83FE67E' \
  --header "Token: $access_token" \
  --output-document 'ev-box.lic' \
  'http://192.168.1.138/ev-amp-store/api/ev/direct/centerAuth/lic/download?centerAuthId=253'

\cp -rf ev-box.lic /data/ev-box/license/ev-box.lic
echo "新算法手动授权成功"

# 重启盒子
box restart
echo "finish install algo,please open 极视角AI一体机边管平台"


---------------------------------------------------------------------------------
host_ip="192.168.1.141"
vim /data/ev-box/storage/10852/run.conf 打开文件内容如下:
{
    "begin_time": "00:00:00",
    "end_time": "23:59:59",
    "call_back": "http://127.0.0.1:7998/api/open/callback/handle",
    "stream_callback":  "",
    "api_version" : 2
}
将上'run.conf'面的'127.0.0.1'修改改成"192.168.1.141" ，通过shell实现




#!/bin/bash

# 指定要修改的IP地址
new_ip="192.168.1.141"

# 指定要修改的配置文件路径
config_file="/data/ev-box/storage/10852/run.conf"

# 将IP地址修改为指定的值
sed -i "s/\"call_back\": \"http:\/\/127.0.0.1:7998\/api\/open\/callback\/handle\",/\"call_back\": \"http:\/\/$new_ip:7998\/api\/open\/callback\/handle\",/" "$config_file"



# 指定要修改的配置文件路径
config_file="/data/ev-box/storage/10852/run.conf"

# 替换IP地址并修改配置文件
sed -i "s/\"call_back\": \"http:\/\/.*\/api\/open\/callback\/handle\"/\"call_back\": \"http:\/\/$new_ip:7998\/api\/open\/callback\/handle\"/" "$config_file"


#!/bin/bash

# 指定要修改的IP地址
new_ip="192.168.1.141"

# 指定要修改的配置文件路径
config_file="/data/ev-box/storage/10852/run.conf"

# 替换IP地址并修改配置文件
sed -i "s/\"call_back\": \"http:\/\/[^:]*:/\"call_back\": \"http:\/\/$new_ip:/" "$config_file"

#!/bin/bash

# 指定要修改的IP地址
new_ip="192.168.1.141"

# 替换IP地址并修改配置文件
sed -i "s/\(\"call_back\": \"http:\/\/\)[^:]*\(:[0-9]\{1,\}\/api\/open\/callback\/handle\"\)/\1$new_ip\2/" /data/ev-box/storage/10852/run.conf
