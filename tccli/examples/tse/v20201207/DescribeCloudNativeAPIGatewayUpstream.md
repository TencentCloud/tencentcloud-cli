**Example 1: 获取云原生网关服务详情下的Upstream列表**

获取云原生网关服务详情下的Upstream列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayUpstream --cli-unfold-argument  \
    --GatewayId gateway-9abf3b70 \
    --ServiceName test-service
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d",
        "Result": {
            "UpstreamList": [
                {
                    "Name": "ins-102555d0.1105a4ef-567b-49c5-8564-0377dae7a5d1.DEFAULT_GROUP__test-dev.default",
                    "ID": "6ca025ec-ba14-4876-b99c-741c1dcc4131",
                    "Target": [
                        {
                            "Host": "1.1.1.1",
                            "Port": 7777,
                            "Weight": 10
                        },
                        {
                            "Host": "1.1.1.1",
                            "Port": 8889,
                            "Weight": 10
                        }
                    ]
                },
                {
                    "Name": "test-upstream",
                    "ID": "7cf1d268-4c76-4caf-8a59-20bb6a3ff016",
                    "Target": [
                        {
                            "Host": "9.0.0.1",
                            "Port": 80,
                            "Weight": 100
                        }
                    ]
                }
            ]
        }
    }
}
```

