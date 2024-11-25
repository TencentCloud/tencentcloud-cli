**Example 1: 查询云原生网关服务列表**

查询云原生网关服务列表


Input: 

```
tccli tse DescribeCloudNativeAPIGatewayServices --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Key app \
    --Filters.0.Value learn
```

Output: 
```
{
    "Response": {
        "RequestId": "d9eb7e29-7800-4327-b37a-67e250dfc147",
        "Result": {
            "ServiceList": [
                {
                    "Name": "service1",
                    "ID": "67695fc9-6d40-4450-83b5-ea57babbad6d",
                    "UpstreamInfo": {
                        "Host": "default-67695fc9-6d40-4450-83b5-ea57babbad6d",
                        "Targets": [
                            {
                                "Host": "10.0.0.121",
                                "Port": 18080,
                                "Weight": 1000,
                                "Health": "HEALTHCHECKS_OFF",
                                "CreatedTime": "2024-11-25 10:51:28",
                                "Source": ""
                            }
                        ],
                        "Algorithm": "round-robin",
                        "HealthStatus": "HEALTHCHECKS_OFF"
                    },
                    "UpstreamType": "IPList",
                    "Editable": true,
                    "Tags": [
                        "TSE-Service-Type:IPList",
                        "TSE-Upstream-SlowStart:0",
                        "TSE-Upstream-Algorithm:round-robin"
                    ],
                    "CreatedTime": "2024-10-22 16:38:26",
                    "Path": null
                }
            ],
            "TotalCount": 1
        }
    }
}
```

