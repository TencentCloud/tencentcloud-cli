**Example 1: 修改实例配置**



Input: 

```
tccli igtm ModifyInstanceConfig --cli-unfold-argument  \
    --InstanceConfig.InstanceName 测试实例 1 \
    --InstanceConfig.Domain xxxx.xxxx.xxxxxxxx@exmaple.com \
    --InstanceConfig.AccessType CUSTOM \
    --InstanceConfig.AccessDomain exmaple-access.com \
    --InstanceConfig.AccessSubDomain xxxx.xxxx.xxxxxxxx.access \
    --InstanceConfig.Remark 测试实例 \
    --InstanceConfig.GlobalTtl 300
```

Output: 
```
{
    "Response": {
        "Instance": {
            "InstanceName": "测试实例 1",
            "InstanceId": "gtm-xxxxxxxxxxx",
            "ResourceId": "",
            "Domain": "xxxx.xxxx.xxxxxxxx@exmaple.com",
            "AccessType": "CUSTOM",
            "AccessDomain": "exmaple-access.com",
            "AccessSubDomain": "xxxx.xxxx.xxxxxxxx.access",
            "GlobalTtl": 300,
            "PackageType": "FREE",
            "WorkingStatus": "NORMAL",
            "Status": "ENABLED",
            "Remark": "测试实例",
            "StrategyNum": 0,
            "AddressPoolNum": 0,
            "MonitorNum": 0,
            "CreatedOn": "2023-12-20 06:43:16",
            "UpdatedOn": "2023-12-26 20:00:03",
            "NotifyEventSet": []
        },
        "RequestId": "be7d3d39-82cf-41e8-9b60-151e9745c422"
    }
}
```

