**Example 1: 更新单个镜像仓库详细信息**



Input: 

```
tccli tcss UpdateAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Username xx \
    --Name xx \
    --Url xx \
    --RegistryVersion xx \
    --RegistryRegion xx \
    --NetType xx \
    --Password xx \
    --RegistryType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "NameRepeatErr": "xx",
        "HealthCheckErr": "xx",
        "RegistryId": 4
    }
}
```

