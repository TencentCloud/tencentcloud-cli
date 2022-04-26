**Example 1: 简单参数升级启动配置**

只传必传的启动配置名称，实例机型，镜像ID，其他均采用系统默认值，具体配置如下：启动配置名称为：as_test，实例机型为：标准2型 1C1G（S2.SMALL1），镜像ID为：img-8toqc6s3。

Input: 

```
tccli as UpgradeLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationId asc-gj14vczi \
    --LaunchConfigurationName as_test \
    --InstanceTypes S2.SMALL1 \
    --ImageId img-8toqc6s3
```

Output: 
```
{
    "Response": {
        "RequestId": "d68a3364-a933-4664-bee4-fb89b8c69b49"
    }
}
```

**Example 2: 详细参数升级启动配置**

启动配置名称为：as_test，镜像ID为：img-8toqc6s3，选择机型为：标准2型 1C1G（S2.SMALL1），系统盘选择 50G 本地硬盘，数据盘选择100G 普通云硬盘，公网付费模式为流量按小时后付费，外网带宽上限 5 Mbps，分配公网IP，选择密钥登录，安装云监控云安全。

Input: 

```
tccli as UpgradeLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationId asc-gj14vczi \
    --LaunchConfigurationName as_test \
    --ImageId img-8toqc6s3 \
    --InstanceTypes S2.SMALL1 \
    --SystemDisk.DiskType LOCAL_BASIC \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_BASIC \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DeleteWithInstance TRUE \
    --DataDisks.0.Encrypt FALSE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 5 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --LoginSettings.KeyIds skey-k8eypc1l \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "1430a2d3-eb73-44c6-8316-218c4562a85c"
    }
}
```

