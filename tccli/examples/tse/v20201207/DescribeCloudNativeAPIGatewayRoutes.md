**Example 1: 查询云原生网关路由列表**

查询云原生网关路由列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRoutes --cli-unfold-argument  \
    --GatewayId abc \
    --Limit 0 \
    --Offset 0 \
    --ServiceName abc \
    --RouteName abc \
    --Filters.0.Key abc \
    --Filters.0.Value abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "RouteList": [
                {
                    "Name": "abc",
                    "ID": "abc",
                    "Methods": [
                        "abc"
                    ],
                    "Paths": [
                        "abc"
                    ],
                    "Hosts": [
                        "abc"
                    ],
                    "Protocols": [
                        "abc"
                    ],
                    "PreserveHost": true,
                    "HttpsRedirectStatusCode": 0,
                    "StripPath": true,
                    "CreatedTime": "abc",
                    "ForceHttps": true,
                    "ServiceName": "abc",
                    "ServiceID": "abc",
                    "DestinationPorts": [
                        1
                    ],
                    "Headers": {
                        "Key": "abc",
                        "Value": "abc"
                    }
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

