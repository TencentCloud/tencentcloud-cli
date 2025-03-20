**Example 1: 正常的获取**

正常的获取

Input: 

```
tccli tcss DescribeAssetImageRegistryRegistryDetail --cli-unfold-argument  \
    --RegistryId 8329
```

Output: 
```
{
    "Response": {
        "ConnDetectDetail": [
            {
                "ConnDetectMessage": "ConnDetectMessage",
                "ConnDetectStatus": "status_connected",
                "FailReason": "FailReason",
                "Quuid": "backend",
                "Solution": "Solution",
                "Uuid": "backend"
            }
        ],
        "Insecure": 1,
        "Name": "jfrog****",
        "NetType": "public",
        "Password": "Aa8888****",
        "RegistryRegion": "ap-beijing",
        "RegistryType": "harbor",
        "RegistryVersion": "v1",
        "RequestId": "ff82bfdb-f923-4b66-8c70-cba784e8be67",
        "SpeedLimit": 1000,
        "Url": "http://good.com.cn",
        "Username": "test-user-name"
    }
}
```

**Example 2: 镜像仓库详情**

镜像仓库详情

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
        "Name": "jfrog****",
        "Username": "test-user",
        "Password": "test-passwd",
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

