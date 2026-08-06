**Example 1: 查询**



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

