**Example 1: 查询云原生网关路由列表**

查询云原生网关路由列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRoutes --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Limit 20 \
    --Offset 0 \
    --ServiceName svc1 \
    --RouteName route1 \
    --Filters.0.Key name \
    --Filters.0.Value global
```

Output: 
```
{
    "Response": {
        "RequestId": "d4dad8c0-7634-474a-ba7b-22e3e5b45911",
        "Result": {
            "RouteList": [
                {
                    "Name": "route1",
                    "ID": "d751b7fa-afcb-479c-818b-d1957432b246",
                    "Methods": [
                        "GET"
                    ],
                    "Paths": [
                        "/v1/users"
                    ],
                    "Hosts": [
                        "tencent.com"
                    ],
                    "Protocols": [
                        "http",
                        "https"
                    ],
                    "PreserveHost": false,
                    "ForceHttps": false,
                    "HttpsRedirectStatusCode": 426,
                    "StripPath": true,
                    "CreatedTime": "2024-11-25 10:49:23",
                    "DestinationPorts": [],
                    "ServiceName": "svc1",
                    "ServiceID": "67695fc9-6d40-4450-83b5-ea57baaaad6d",
                    "Headers": [
                        {
                            "Key": "app",
                            "Value": "learn"
                        }
                    ]
                }
            ],
            "TotalCount": 1
        }
    }
}
```

