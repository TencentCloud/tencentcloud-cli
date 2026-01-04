**Example 1: 查询成功**



Input: 

```
tccli tdmq DescribeRocketMQGeneralSKUs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Skus": [
            {
                "OnSale": true,
                "PriceTags": [
                    {
                        "Category": "v_tdmq_instance_specification",
                        "Code": "sv_tdmq_pro_c_general",
                        "Name": "tps",
                        "Step": 1
                    }
                ],
                "SkuCode": "general_8k",
                "TopicNumLimit": 400,
                "TopicNumUpperLimit": 2000,
                "TpsLimit": 8000
            }
        ],
        "RequestId": "2da7fbba-4ddc-4c64-9935-8e35ce825f5a"
    }
}
```

