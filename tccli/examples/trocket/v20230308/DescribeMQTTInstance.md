**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTInstance --cli-unfold-argument  \
    --InstanceId mqtt-7pnqmkrx
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ClientNumLimit": 1000,
        "CreatedTime": 1705562417,
        "InstanceId": "mqtt-7pnqmkrx",
        "InstanceName": "sunjianxiong-1",
        "InstanceStatus": "RUNNING",
        "InstanceType": "BASIC",
        "Remark": "this is remark",
        "RequestId": "2251b9cf-aedd-4457-ac8d-bc705f48ccb8",
        "SkuCode": "basic_1k",
        "SubscriptionNumLimit": 1000,
        "TopicNum": 1,
        "TopicNumLimit": 25,
        "TpsLimit": 1000
    }
}
```

