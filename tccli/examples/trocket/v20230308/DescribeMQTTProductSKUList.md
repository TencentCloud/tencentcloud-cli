**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTProductSKUList --cli-unfold-argument ```

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
                "ProxySpecCore": 2,
                "ProxySpecCount": 1,
                "ProxySpecMemory": 4,
                "SkuCode": "mqtt_1k",
                "SubscriptionNumLimit": 1,
                "TopicNumLimit": 1,
                "TpsLimit": 1
            },
            {
                "ClientNumLimit": 1000,
                "InstanceType": "BASIC",
                "OnSale": true,
                "ProxySpecCore": 1,
                "ProxySpecCount": 2,
                "ProxySpecMemory": 2,
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNumLimit": 25,
                "TpsLimit": 1000
            }
        ],
        "RequestId": "2be05982-b125-4259-b965-c487949cd896",
        "TotalCount": 2
    }
}
```

