**Example 1: 新增单个镜像仓库详细信息**



Input: 

```
tccli tcss AddAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Username usename \
    --Name test \
    --Url http://127.0.0.1:8080 \
    --RegistryVersion V2 \
    --RegistryRegion default \
    --NetType public \
    --Password xxx \
    --RegistryType harbor
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

