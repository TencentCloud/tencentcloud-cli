**Example 1: 更新单个镜像仓库详细信息**

更新单个镜像仓库详细信息

Input: 

```
tccli tcss UpdateAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Name test \
    --NetType public \
    --Password xxx \
    --RegistryRegion default \
    --RegistryType harbor \
    --RegistryVersion V2 \
    --Url http://127.0.0.1:8080 \
    --Username username
```

Output: 
```
{
    "Response": {
        "HealthCheckErr": "abc",
        "NameRepeatErr": "abc",
        "RegistryId": 0,
        "RequestId": "abc"
    }
}
```

