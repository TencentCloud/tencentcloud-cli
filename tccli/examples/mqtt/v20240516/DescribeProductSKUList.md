**Example 1: 示例**

示例

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
                "ClientNumLimit": 1,
                "InstanceType": "BASIC",
                "OnSale": true,
                "SkuCode": "mqtt_1k",
                "TopicNumLimit": 1,
                "TpsLimit": 1
            },
            {
                "ClientNumLimit": 1000,
                "InstanceType": "BASIC",
                "OnSale": true,
                "SkuCode": "basic_1k",
                "TopicNumLimit": 25,
                "TpsLimit": 1000
            }
        ],
        "RequestId": "2be05982-b125-4259-b965-c487949cd896",
        "TotalCount": 2
    }
}
```

