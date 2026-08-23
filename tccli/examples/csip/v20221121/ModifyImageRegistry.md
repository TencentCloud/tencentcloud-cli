**Example 1: 修改镜像仓库信息**



Input: 

```
tccli csip ModifyImageRegistry --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Name ccr-default \
    --Username default-user \
    --Password default-password \
    --Url https://ccr.ccs.tencentyun.com \
    --RegistryType ccr \
    --NetType public \
    --RegistryVersion 1.0 \
    --RegistryRegion ap-guangzhou \
    --SpeedLimit 50 \
    --Insecure 0 \
    --NeedScan True \
    --SyncMode 0 \
    --InstanceId ccr-instance \
    --ConnectivityDetectConfig.0.Quuid backend \
    --ConnectivityDetectConfig.0.Uuid backend \
    --Id 5
```

Output: 
```
{
    "Response": {
        "RegistryId": 5,
        "RequestId": "359e7e65-cd0c-4293-85a3-b5fb249c383a"
    }
}
```

