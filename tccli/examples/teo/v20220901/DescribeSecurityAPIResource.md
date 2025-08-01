**Example 1: 查询指定站点的 API 资源**

分页查询某个站点的 API 资源。

Input: 

```
tccli teo DescribeSecurityAPIResource --cli-unfold-argument  \
    --ZoneId zone-123123232 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "APIResources": [
            {
                "Id": "apires-1230001002",
                "Name": "test2",
                "Path": "/ava",
                "APIServiceIds": [
                    "apisrv-123233399"
                ],
                "Methods": [
                    "POST",
                    "PUT"
                ],
                "RequestConstraint": "${http.request.body.form['operationType']} in ['id.dana.order.listAl']"
            }
        ],
        "RequestId": "97f2dd9b-1624-4519-9ac6-13c95154d846"
    }
}
```

