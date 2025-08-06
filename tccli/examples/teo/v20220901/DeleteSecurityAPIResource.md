**Example 1: 删除指定 API 资源**

删除某些已有的 API 资源。

Input: 

```
tccli teo DeleteSecurityAPIResource --cli-unfold-argument  \
    --ZoneId zone-123sfakjf \
    --APIResourceIds apires-1232000001 apires-1232000002
```

Output: 
```
{
    "Response": {
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

