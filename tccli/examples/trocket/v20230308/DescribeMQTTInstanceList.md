**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTInstanceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ClientNumLimit": 1,
                "CreateTime": 1705565760,
                "InstanceId": "mqtt-wjgxr8jg",
                "InstanceName": "su-0118-no-pub",
                "InstanceStatus": "CREATE_FAILURE",
                "InstanceType": "BASIC",
                "Remark": "",
                "SkuCode": "mqtt_1k",
                "SubscriptionNumLimit": 1,
                "TopicNum": 0,
                "TopicNumLimit": 1,
                "TpsLimit": 1,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705391046,
                "InstanceId": "mqtt-47ka4rdr",
                "InstanceName": "sun-0116",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 25,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            }
        ],
        "RequestId": "9424369d-904f-4fa2-b407-0bd5e536e989",
        "TotalCount": 10
    }
}
```

