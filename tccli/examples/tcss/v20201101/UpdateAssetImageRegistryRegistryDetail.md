**Example 1: 更新单个镜像仓库详细信息**

更新单个镜像仓库详细信息

Input: 

```
tccli tcss UpdateAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Name private_aws \
    --Username AKIAVHDIU6R7C3BD \
    --Password password \
    --Url https://dkr.ecr.us-east-119.amazonaws.com \
    --RegistryType aws \
    --RegistryVersion V1 \
    --NetType public \
    --RegistryRegion default \
    --SpeedLimit 0 \
    --Insecure 0 \
    --ConnDetectConfig.0.Quuid backend \
    --ConnDetectConfig.0.Uuid backend
```

Output: 
```
{
    "Response": {
        "HealthCheckErr": "",
        "NameRepeatErr": "",
        "RegistryId": 29113,
        "RequestId": "47d03bf3-6ea3-4e79-a7f0-70eae99717bc"
    }
}
```

