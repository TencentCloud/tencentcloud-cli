**Example 1: 获取产品规格信息**

获取产品规格信息

Input: 

```
tccli trocket DescribeProductSKUs --cli-unfold-argument ```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "DefaultRetention": 72,
                "GroupNumLimit": 500,
                "InstanceType": "EXPERIMENT",
                "MaxMessageDelay": 48,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Name": "tps"
                    }
                ],
                "RetentionLowerLimit": 24,
                "RetentionUpperLimit": 72,
                "ScaledTpsLimit": 0,
                "SkuCode": "experiment_500",
                "TopicNumLimit": 50,
                "TpsLimit": 500
            },
            {
                "DefaultRetention": 72,
                "GroupNumLimit": 500,
                "InstanceType": "BASIC",
                "MaxMessageDelay": 168,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Name": "tps"
                    }
                ],
                "RetentionLowerLimit": 24,
                "RetentionUpperLimit": 72,
                "ScaledTpsLimit": 0,
                "SkuCode": "basic_1k",
                "TopicNumLimit": 50,
                "TpsLimit": 1000
            },
            {
                "DefaultRetention": 72,
                "GroupNumLimit": 500,
                "InstanceType": "BASIC",
                "MaxMessageDelay": 168,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Name": "tps"
                    }
                ],
                "RetentionLowerLimit": 24,
                "RetentionUpperLimit": 72,
                "ScaledTpsLimit": 0,
                "SkuCode": "basic_2k",
                "TopicNumLimit": 50,
                "TpsLimit": 2000
            },
            {
                "DefaultRetention": 72,
                "GroupNumLimit": 500,
                "InstanceType": "BASIC",
                "MaxMessageDelay": 168,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Name": "tps"
                    }
                ],
                "RetentionLowerLimit": 24,
                "RetentionUpperLimit": 72,
                "ScaledTpsLimit": 0,
                "SkuCode": "basic_4k",
                "TopicNumLimit": 50,
                "TpsLimit": 4000
            },
            {
                "DefaultRetention": 72,
                "GroupNumLimit": 500,
                "InstanceType": "BASIC",
                "MaxMessageDelay": 168,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Name": "tps"
                    }
                ],
                "RetentionLowerLimit": 24,
                "RetentionUpperLimit": 72,
                "ScaledTpsLimit": 0,
                "SkuCode": "basic_6k",
                "TopicNumLimit": 50,
                "TpsLimit": 6000
            }
        ],
        "RequestId": "010e2991-4b01-40f9-a4a6-30bdfb175448"
    }
}
```

