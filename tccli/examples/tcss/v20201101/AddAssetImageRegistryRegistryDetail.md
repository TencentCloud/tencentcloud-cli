**Example 1: 新增单个镜像仓库详细信息**



Input: 

```
tccli tcss AddAssetImageRegistryRegistryDetail --cli-unfold-argument  \
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

