**Example 1: 查询**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPRouteList --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId f8d4b985-641f-4010-a202-4559af81df6d \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CreateTime": "2026-07-03T14:49:00+08:00",
                    "Expression": "http.headers.x_tenant == \"tenant-a\"",
                    "HeaderMatch": [
                        {
                            "Key": "X-Tenant",
                            "MatchType": "Exact",
                            "Value": "tenant-a"
                        }
                    ],
                    "IsDefault": false,
                    "Methods": [],
                    "Name": "route-with-preserve-host",
                    "Path": "",
                    "PathMatchType": "",
                    "Priority": 2000,
                    "RouteId": "791a27f9-0431-4d71-87e3-511a650cc760",
                    "Status": "Disabled"
                }
            ],
            "TotalCount": 3
        },
        "RequestId": "146775a2-b638-43d0-8a7b-906d0bc408d5"
    }
}
```

