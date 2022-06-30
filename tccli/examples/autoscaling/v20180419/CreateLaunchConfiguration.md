**Example 1: 简单参数创建**

只传必传的启动配置名称，实例机型，镜像ID，其他均采用系统默认值，具体配置如下：启动配置名称为：as_test，实例机型为：标准2型 1C1G（S2.SMALL1），镜像ID为：img-8toqc6s3。

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --ImageId img-8toqc6s3 \
    --InstanceType S2.SMALL1 \
    --LaunchConfigurationName as_test
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-23h37kyn",
        "RequestId": "d639dd64-9e46-4246-b13c-80954f81c11b"
    }
}
```

**Example 2: 详细参数创建**

启动配置名称为：as_test，镜像ID为：img-8toqc6s3，选择机型为：标准2型 1C1G（S2.SMALL1），系统盘选择 50G 本地硬盘，数据盘选择100G 普通云硬盘，实例销毁时不保留数据盘，数据盘不加密，公网付费模式为流量按小时后付费，外网带宽上限 5 Mbps，分配公网IP，选择密钥登录，安装云监控云安全。

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType LOCAL_BASIC \
    --LoginSettings.KeyIds skey-k8eypc1l \
    --ImageId img-8toqc6s3 \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --LaunchConfigurationName as_test \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 5 \
    --InstanceType S2.SMALL1 \
    --DataDisks.0.Encrypt FALSE \
    --DataDisks.0.DeleteWithInstance TRUE \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_BASIC
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-fdz8j7dh",
        "RequestId": "9a7209d3-2260-49d7-952a-dfa2001f8822"
    }
}
```

**Example 3: 创建竞价实例配置**

启动配置名称为：spot-test，机型为：标准2型 2C4G（S2.MEDIUM4），计费配置为竞价（SPOTPAID），最高出价为0.99元/小时。

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceMarketOptions.SpotOptions.SpotInstanceType one-time \
    --InstanceMarketOptions.SpotOptions.MaxPrice 0.99 \
    --InstanceMarketOptions.MarketType spot \
    --ImageId img-8toqc6s3 \
    --InstanceChargeType SPOTPAID \
    --LaunchConfigurationName spot-test \
    --InternetAccessible.PublicIpAssigned true \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 20 \
    --InstanceType S2.MEDIUM4
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-hpzwe3o2",
        "RequestId": "ccfe3052-e9c9-47ee-bf3d-5bc2dfd972c0"
    }
}
```

**Example 4: 创建启动配置，支持多种实例机型**

支持两种实例机型，分别是S2.SMALL2和S2.SMALL4

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --ImageId img-8toqc6s3 \
    --InstanceTypes S2.SMALL4 S2.SMALL2 \
    --LaunchConfigurationName multi_instance_types
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-77mh1cho",
        "RequestId": "2864c860-27a0-439e-a1e1-0003b76734e7"
    }
}
```

