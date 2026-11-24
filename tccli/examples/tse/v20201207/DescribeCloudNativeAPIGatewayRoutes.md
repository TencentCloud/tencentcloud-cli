**Example 1: 按服务查询路由**

查询指定服务的路由。

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRoutes --cli-unfold-argument  \
    --GatewayId gateway-3d000b5d \
    --ServiceId 55caa77b-7d90-4e2c-b6e0-6ed4026920eb \
    --RouteTypes Original Gray \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "767761a7-3500-4f55-b8cf-b40719d95032",
        "Result": {
            "RouteList": [
                {
                    "Name": "std-websocket",
                    "ID": "019b6377-f2b4-437a-9b01-1773be858265",
                    "Methods": null,
                    "Paths": [
                        "/std/ws"
                    ],
                    "Hosts": null,
                    "Protocols": [
                        "http"
                    ],
                    "PreserveHost": true,
                    "ForceHttps": false,
                    "HttpsRedirectStatusCode": 426,
                    "RegexPriority": 0,
                    "StripPath": false,
                    "CreatedTime": "2026-11-10 20:27:24",
                    "DestinationPorts": [],
                    "ServiceName": "std-k8s-http",
                    "ServiceID": "55caa77b-7d90-4e2c-b6e0-6ed4026920eb",
                    "Headers": [],
                    "RequestBuffering": true,
                    "ResponseBuffering": true,
                    "RouteSource": "Original",
                    "TimeoutSource": "Service"
                }
            ],
            "TotalCount": 5
        }
    }
}
```

**Example 2: 查询**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayRoutes --cli-unfold-argument  \
    --GatewayId gateway-5796a718
```

Output: 
```
{
    "Response": {
        "RequestId": "2929fa42-0493-4629-9c08-e6637950c378",
        "Result": {
            "RouteList": [
                {
                    "CreatedTime": "2026-07-13 14:26:25",
                    "DestinationPorts": [],
                    "ForceHttps": false,
                    "Headers": [],
                    "Hosts": null,
                    "HttpsRedirectStatusCode": 426,
                    "ID": "fdb7a827-f99a-4b6a-a2c6-dbe077796aa4",
                    "Methods": null,
                    "Name": null,
                    "Paths": [
                        "/huidu"
                    ],
                    "PreserveHost": false,
                    "Protocols": [
                        "http",
                        "https"
                    ],
                    "RegexPriority": 0,
                    "RequestBuffering": true,
                    "ResponseBuffering": true,
                    "RouteSource": "Original",
                    "ServiceID": "557a0cd8-87b8-40b1-a1d8-4d49ab70423b",
                    "ServiceName": "huidu-bench",
                    "StripPath": true
                }
            ],
            "TotalCount": 1
        }
    }
}
```

