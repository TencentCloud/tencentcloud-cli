**Example 1: 获取购买配置**



Input: 

```
tccli tdmq DescribePurchaseConfig --cli-unfold-argument  \
    --Type 0
```

Output: 
```
{
    "Response": {
        "Regions": [
            {
                "RegionId": 1,
                "Zones": [
                    {
                        "ZoneId": 1,
                        "Products": [
                            {
                                "Name": "devName",
                                "MaxNodes": 1,
                                "MinNodes": 1,
                                "SoldOut": true,
                                "SingleMinNodes": 0,
                                "SingleMaxNodes": 0
                            }
                        ]
                    }
                ],
                "MaxStorage": 1,
                "MinStorage": 1,
                "Available": true
            }
        ],
        "Products": [
            {
                "MaxDelayedMessages": 200,
                "Name": "DevName",
                "Tps": 1,
                "Topic": 1,
                "Throughput": 1,
                "BasicSvCode": "sv_tdmq_pro_c_basic_1",
                "NodeSvCode": "sv_tdmq_pro_c_node_1",
                "DisplayName": "devTest",
                "Remark": "devRemark",
                "IsRecommended": true,
                "MaxNamespaces": 1,
                "MaxTopics": 1,
                "Queues": 1,
                "Connections": 1,
                "Deployment": 0,
                "Environment": 0,
                "BillingLabelVersion": "P1",
                "MaxZones": 0,
                "MaxSumPartitions": 0
            }
        ],
        "RequestId": "asdaaddas-dfasaasd-afdfassad-sddfs"
    }
}
```

