**Example 1: 更新单个镜像仓库详细信息**

更新单个镜像仓库详细信息

Input: 

```
tccli tcss UpdateAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Name private_aws \
    --Username name01 \
    --Password password \
    --Url https://dkr.ecr.us-east-119.amazonaws.com \
    --RegistryType aws \
    --RegistryVersion V1 \
    --NetType public \
    --RegistryRegion default \
    --SpeedLimit 0 \
    --Insecure 0 \
    --ConnDetectConfig.0.Quuid 5a540076-d38a-4078-aa98-e7c86371d322 \
    --ConnDetectConfig.0.Uuid 5a540076-d38a-4078-aa98-e7c86371d322
```

Output: 
```
{
    "Response": {
        "HealthCheckErr": "connect refused",
        "NameRepeatErr": "connect refused",
        "RegistryId": 29113,
        "RequestId": "47d03bf3-6ea3-4e79-a7f0-70eae99717bc"
    }
}
```

