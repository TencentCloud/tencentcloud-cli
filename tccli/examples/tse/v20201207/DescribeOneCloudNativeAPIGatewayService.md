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
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d",
        "Result": {
            "Name": "test-service",
            "ID": "77748647-7b59-4c94-853e-5a96b72cab1f",
            "Protocol": "http",
            "Path": "/",
            "Timeout": 5000,
            "Retries": 3,
            "Tags": [
                "TSE-Upstream-Type:HostIP"
            ],
            "UpstreamInfo": {
                "Host": "8.8.8.8",
                "Port": 60,
                "Targets": null
            },
            "UpstreamType": "HostIP",
            "Editable": true
        }
    }
}
```

