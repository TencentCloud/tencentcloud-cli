**Example 1: 轻量查询云原生网关服务列表**

轻量查询云原生网关服务列表


Input: 

```
tccli tse DescribeCloudNativeAPIGatewayServicesLight --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Key id \
    --Filters.0.Value d9eb7e29-7800-4327-b37a-67e250dfc147
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
                                "CreatedTime": "2024-11-25 10:51:28"
                            }
                        ]
                    },
                    "UpstreamType": "IPList",
                    "CreatedTime": "2024-10-22 16:38:26",
                    "Path": ""
                }
            ],
            "TotalCount": 1
        }
    }
}
```

