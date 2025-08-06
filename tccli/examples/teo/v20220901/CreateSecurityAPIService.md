**Example 1: 创建 API 服务**

新建一个 API 服务。

Input: 

```
tccli teo CreateSecurityAPIService --cli-unfold-argument  \
    --ZoneId zone-123sfakjf \
    --APIServices.0.Name test \
    --APIServices.0.BasePath /tt
```

Output: 
```
{
    "Response": {
        "APIServiceIds": [
            "apisrv-1232382313"
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

