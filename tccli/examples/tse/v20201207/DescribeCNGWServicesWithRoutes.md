**Example 1: 示例**



Input: 

```
tccli tse DescribeCNGWServicesWithRoutes --cli-unfold-argument  \
    --GatewayId gateway-2c8a4896 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ServiceList": [
                {
                    "RouteHasMore": false,
                    "RouteTotalCount": 1,
                    "Routes": [
                        {
                            "CreatedTime": "2026-07-25 16:26:52",
                            "DestinationPorts": [],
                            "ForceHttps": false,
                            "Headers": [],
                            "Hosts": null,
                            "HttpsRedirectStatusCode": 426,
                            "ID": "0a6919f3-0d86-4413-9cac-1bc6af54ace3",
                            "Methods": [
                                "ANY"
                            ],
                            "Name": "mirror",
                            "Paths": [
                                "/mirror"
                            ],
                            "PreserveHost": false,
                            "Protocols": [
                                "http"
                            ],
                            "RegexPriority": 0,
                            "RequestBuffering": true,
                            "ResponseBuffering": true,
                            "ServiceID": "092cf1ac-a840-4359-bc6b-448318ee6361",
                            "ServiceName": "mirror",
                            "StripPath": true
                        }
                    ],
                    "Service": {
                        "CreatedTime": "2026-07-25 16:24:33",
                        "Editable": true,
                        "ID": "092cf1ac-a840-4359-bc6b-448318ee6361",
                        "Name": "mirror",
                        "Path": "/",
                        "Tags": [
                            "TSE-Service-Type:Kubernetes"
                        ],
                        "UpstreamInfo": {
                            "Algorithm": "round-robin",
                            "HealthStatus": "HEALTHCHECKS_OFF",
                            "Namespace": "traffic-mirror-test",
                            "Port": 8889,
                            "RealSourceType": "EKS",
                            "ServiceName": "mirror-target",
                            "SourceID": "cls-koqdd0fq",
                            "SourceName": "【勿删除】tre-压测",
                            "SourceType": "EKS",
                            "Targets": [
                                {
                                    "CreatedTime": "2026-07-27 18:53:10",
                                    "Health": "HEALTHCHECKS_OFF",
                                    "Host": "10.0.20.81",
                                    "Port": 8889,
                                    "Source": "",
                                    "Weight": 100
                                }
                            ]
                        },
                        "UpstreamType": "Kubernetes"
                    }
                }
            ],
            "TotalCount": 2
        },
        "RequestId": "4f2d9b87-9867-4414-a89b-2392ae4d07e7"
    }
}
```

