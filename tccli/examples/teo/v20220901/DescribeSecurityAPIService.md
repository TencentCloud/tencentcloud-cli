**Example 1: 查询指定站点的 API 服务**

分页查询指定站点的 API 服务。

Input: 

```
tccli teo DescribeSecurityAPIService --cli-unfold-argument  \
    --ZoneId zone-123123232 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "APIServices": [
            {
                "Id": "apisrv-1230001001",
                "Name": "test1",
                "BasePath": "/tt"
            }
        ],
        "RequestId": "97f2dd9b-1624-4519-9ac6-13c95154d846"
    }
}
```

