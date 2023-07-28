**Example 1: 新增单个镜像仓库详细信息**

新增单个镜像仓库详细信息

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
        "HealthCheckErr": "abc",
        "NameRepeatErr": "abc",
        "RegistryId": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: 正常添加**

正常添加

Input: 

```
tccli tcss AddAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --Name abc \
    --Username abc \
    --Password abc \
    --Url abc \
    --RegistryType abc \
    --RegistryVersion abc \
    --NetType abc \
    --RegistryRegion abc \
    --SpeedLimit 0 \
    --Insecure 1 \
    --ConnDetectConfig.0.Quuid abc \
    --ConnDetectConfig.0.Uuid abc
```

Output: 
```
{
    "Response": {
        "HealthCheckErr": "",
        "NameRepeatErr": "",
        "RegistryId": 8329,
        "RequestId": "f8d97649-ca1b-4f94-8ed4-40052a40d426"
    }
}
```

