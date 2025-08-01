**Example 1: 删除指定 API 服务**

删除某些已有的 API 服务。

Input: 

```
tccli teo DeleteSecurityAPIService --cli-unfold-argument  \
    --ZoneId zone-123sfakjf \
    --APIServiceIds apisrv-1232382313 apisrv-1232382314
```

Output: 
```
{
    "Response": {
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

