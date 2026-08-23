**Example 1: 添加镜像仓库信息**



Input: 

```
tccli csip AddImageRegistry --cli-unfold-argument  \
    --Name 测试环境内网harbor \
    --Username admin \
    --Password Har******** \
    --Url http://172.16.0.25 \
    --RegistryType harbor \
    --NetType public \
    --RegistryVersion 1.0 \
    --RegistryRegion ap-guangzhou \
    --SpeedLimit 50 \
    --Insecure 1 \
    --NeedScan False \
    --SyncMode 0 \
    --InstanceId harbor-instance \
    --ConnectivityDetectConfig.0.Quuid 2d85debe-8049-****-****-2f29000a6a23 \
    --ConnectivityDetectConfig.0.Uuid 2d85debe-8049-****-****-2f29000a6a23
```

Output: 
```
{
    "Response": {
        "RegistryId": 33,
        "RequestId": "cff2e236-e654-4db3-baf5-3f97e4c891ba"
    }
}
```

