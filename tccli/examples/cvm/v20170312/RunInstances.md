**Example 1: 独享子机购买**

实例所在位置为上海二区，在专用宿主机host-q88gab4i上创建，付费模式为独享子机付费，镜像ID为：img-pmqg1cw7，实例配置为：1C1G，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码为Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceCount 1 \
    --Placement.HostIds host-q88gab4i \
    --Placement.Zone ap-shanghai-2 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7 \
    --InstanceChargeType CDHPAID \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceName QCLOUD-TEST \
    --InstanceType CDH_1C1G \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-0s7wsh5x"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 包年包月实例购买**

实例所在位置为上海二区，付费模式为包年包月，购买一个月，到期自动续费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码为Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceCount 1 \
    --Placement.Zone ap-shanghai-2 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7 \
    --InstanceChargeType PREPAID \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceName QCLOUD-TEST \
    --InstanceType S5.16XLARGE256 \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-bfw5zq3y"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: 最简单参数的购买**

只传必传的Zone和镜像ID，其他均采用系统默认值，具体配置如下：实例所在位置为上海二区，镜像ID为：img-pmqg1cw7。

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-1vogaxgk"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 4: 按小时后付费实例购买**

实例所在位置为上海二区，付费模式为按小时后付费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码为Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceCount 1 \
    --Placement.Zone ap-shanghai-2 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceName QCLOUD-TEST \
    --InstanceType S5.16XLARGE256 \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-32kcaqoa"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 5: 指定私有网络ip创建实例**

实例所在位置为上海二区，付费模式为按小时后付费，镜像ID为：img-dkwyg6sr，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，私有网络，vpcId为1urkhbj4，子网ID为dcs9x3gz，指定私有网络ip为10.0.0.18，10.0.0.19，购买数量为2台。

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --VirtualPrivateCloud.SubnetId subnet-dcs9x3gz \
    --VirtualPrivateCloud.VpcId vpc-1urkhbj4 \
    --VirtualPrivateCloud.PrivateIpAddresses 10.0.0.19 10.0.0.18 \
    --InstanceCount 2 \
    --Placement.Zone ap-shanghai-2 \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --ImageId img-dkwyg6sr \
    --InstanceType S5.16XLARGE256
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-0s7wsh5x",
            "ins-03lw8hok"
        ],
        "RequestId": "3c14def19-cfes-470e-b241-90787u6jf5uj"
    }
}
```

