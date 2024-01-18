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
                "InstanceName": "sunjianxiong-0118-no-pub",
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
                "CreateTime": 1705562417,
                "InstanceId": "mqtt-7pnqmkrx",
                "InstanceName": "sunjianxiong-1",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "this is remark",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705562390,
                "InstanceId": "mqtt-92vrwg7q",
                "InstanceName": "sunjianxiong-1",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "this is remark",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705562343,
                "InstanceId": "mqtt-mzjj8pwq",
                "InstanceName": "sunjianxiong-1",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "this is remark",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705562309,
                "InstanceId": "mqtt-r8wq2qbr",
                "InstanceName": "sunjianxiong",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "this is remark",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705481574,
                "InstanceId": "mqtt-o98e9db4",
                "InstanceName": "sunjianxiong-0117",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 1,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
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
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705386756,
                "InstanceId": "mqtt-3jaepn74",
                "InstanceName": "sunjianxiong",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "this is remark",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1705305132,
                "InstanceId": "mqtt-x4r9v2xq",
                "InstanceName": "sunjianxiong-0115",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 1,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "ClientNumLimit": 1000,
                "CreateTime": 1704962679,
                "InstanceId": "mqtt-o47zowaz",
                "InstanceName": "sjx-0111",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "Remark": "",
                "SkuCode": "basic_1k",
                "SubscriptionNumLimit": 1000,
                "TopicNum": 0,
                "TopicNumLimit": 1000,
                "TpsLimit": 1000,
                "Version": "1"
            }
        ],
        "RequestId": "9424369d-904f-4fa2-b407-0bd5e536e989",
        "TotalCount": 10
    }
}
```

