**Example 1: 示例**



Input: 

```
tccli mqtt DescribeProductSKUList --cli-unfold-argument ```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "MQTTProductSkuList": [
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 2000,
                "InstanceType": "BASIC",
                "MaxSubscriptionPerClient": 30,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Category": "v_tdmq_mqtt_instance_specification",
                        "Code": "sv_tdmq_mqtt_instance_specification_basic_config",
                        "Name": "tps",
                        "Step": 1
                    },
                    {
                        "Category": "v_tdmq_instance_specification",
                        "Code": "sv_tdmq_mqtt_instance_specification_basic_tps",
                        "Name": "stepTps",
                        "Step": 2
                    }
                ],
                "SkuCode": "basic_2k",
                "TopicNumLimit": 100,
                "TpsLimit": 2000
            },
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 5000,
                "InstanceType": "BASIC",
                "MaxSubscriptionPerClient": 30,
                "OnSale": true,
                "PriceTags": [
                    {
                        "Category": "v_tdmq_mqtt_instance_specification",
                        "Code": "sv_tdmq_mqtt_instance_specification_basic_config",
                        "Name": "tps",
                        "Step": 1
                    },
                    {
                        "Category": "v_tdmq_instance_specification",
                        "Code": "sv_tdmq_mqtt_instance_specification_basic_tps",
                        "Name": "stepTps",
                        "Step": 5
                    }
                ],
                "SkuCode": "basic_5k",
                "TopicNumLimit": 100,
                "TpsLimit": 5000
            }
        ],
        "RequestId": "590f4a66-aa96-49d7-9572-0e01e90dc85c",
        "TotalCount": 2
    }
}
```

