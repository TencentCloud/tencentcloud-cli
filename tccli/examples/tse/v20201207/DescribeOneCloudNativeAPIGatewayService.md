**Example 1: 获取云原生网关服务详情**

获取云原生网关服务详情

Input: 

```
tccli tse DescribeOneCloudNativeAPIGatewayService --cli-unfold-argument  \
    --GatewayId gateway-9abf3b70 \
    --Name test-service
```

Output: 
```
{
    "Response": {
        "RequestId": "a4f498d5-4d3a-469b-b47b-bbdf1c7b07a8",
        "Result": {
            "Name": "service1",
            "ID": "67695fc9-6d40-4450-83b5-ea57bazzad6d",
            "Protocol": "http",
            "Path": null,
            "Timeout": 60000,
            "Retries": 5,
            "Tags": [
                "TSE-Service-Type:IPList",
                "TSE-Upstream-SlowStart:0",
                "TSE-Upstream-Algorithm:round-robin"
            ],
            "UpstreamInfo": {
                "Host": "default-67695fc9-6d40-4450-83b5-ea57bazzad6d",
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
            "CreatedTime": "2024-10-22 16:38:26"
        }
    }
}
```

