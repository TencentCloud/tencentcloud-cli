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
        "RequestId": "74a0e9ba-8e65-4124-b525-529cc98a51dc",
        "Regions": [
            {
                "RegionId": 1,
                "MaxStorage": 1000,
                "MinStorage": 100,
                "Zones": [
                    {
                        "ZoneId": 100001,
                        "Products": [
                            {
                                "Name": "vip-basic-1",
                                "MaxNodes": 20,
                                "MinNodes": 2,
                                "SoldOut": false
                            }
                        ]
                    }
                ]
            }
        ],
        "Products": [
            {
                "Name": "vip-basic-1",
                "Tps": 4000,
                "Topic": 6000,
                "Throughput": 480,
                "BasicSvCode": "sv_tdmq_pro_c_basic_1",
                "NodeSvCode": "sv_tdmq_pro_c_node_1"
            }
        ]
    }
}
```

**Example 2: 获取可用区配置**



Input: 

```
tccli tdmq DescribePurchaseConfig --cli-unfold-argument  \
    --Type 0
```

Output: 
```
{
    "Response": {
        "RequestId": "2a4e1aa6-a309-41f0-9fcc-69e8b8f058e6",
        "Regions": [
            {
                "RegionId": 1,
                "MaxStorage": 1000,
                "MinStorage": 100,
                "Zones": [
                    {
                        "ZoneId": 100001,
                        "Products": [
                            {
                                "Name": "vip-basic-1",
                                "MaxNodes": 20,
                                "MinNodes": 2,
                                "SoldOut": false
                            }
                        ]
                    }
                ]
            }
        ],
        "Products": [
            {
                "Name": "vip-basic-1",
                "Tps": 4000,
                "Topic": 6000,
                "Throughput": 480,
                "BasicSvCode": "sv_tdmq_pro_c_basic_1",
                "NodeSvCode": "sv_tdmq_pro_c_node_1",
                "DisplayName": "基础型",
                "Remark": "",
                "IsRecommended": false
            }
        ]
    }
}
```

