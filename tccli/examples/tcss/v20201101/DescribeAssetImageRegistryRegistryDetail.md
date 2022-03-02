**Example 1: 运行时访问控制事件详细信息**



Input: 

```
tccli tcss DescribeAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --RegistryId 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5187d432-1753-4376-81b6-12e1f7e6ecf5",
        "Name": "test",
        "Username": "xxx",
        "Password": "xxx",
        "Url": "https://127.0.0.1:8080",
        "RegistryType": "harbor",
        "RegistryVersion": "v2",
        "NetType": "public",
        "RegistryRegion": "default",
        "SpeedLimit": 1,
        "Insecure": 0
    }
}
```

