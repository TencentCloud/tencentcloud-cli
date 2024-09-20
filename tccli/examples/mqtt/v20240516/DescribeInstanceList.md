**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeInstanceList --cli-unfold-argument  \
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

**Example 2: 样例**

样例

Input: 

```
tccli mqtt DescribeInstanceList --cli-unfold-argument ```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 100,
                "CreateTime": 1721121835,
                "DestroyTime": 0,
                "ExpiryTime": 0,
                "InstanceId": "mqtt-12345678",
                "InstanceName": "mock-instance",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "MaxSubscriptionPerClient": 30,
                "PayMode": "POSTPAID",
                "Remark": "测试无计费order，计费上报",
                "RenewFlag": 0,
                "SkuCode": "basic_1k",
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 100,
                "CreateTime": 1718885863,
                "DestroyTime": 0,
                "ExpiryTime": 1721477863002,
                "InstanceId": "mqtt-g4r4x85z",
                "InstanceName": "sunjianxiong",
                "InstanceStatus": "RUNNING",
                "InstanceType": "PRO",
                "MaxSubscriptionPerClient": 30,
                "PayMode": "PREPAID",
                "Remark": "测试收发用，已配置内网",
                "RenewFlag": 0,
                "SkuCode": "pro_4k_5",
                "TopicNum": 6,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 100,
                "CreateTime": 1718883088,
                "DestroyTime": 0,
                "ExpiryTime": 0,
                "InstanceId": "mqtt-vv9pnwq4",
                "InstanceName": "jehansun-06201930",
                "InstanceStatus": "RUNNING",
                "InstanceType": "PRO",
                "MaxSubscriptionPerClient": 30,
                "PayMode": "POSTPAID",
                "Remark": "",
                "RenewFlag": 0,
                "SkuCode": "pro_4k_5",
                "TopicNum": 0,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 100,
                "CreateTime": 1717663198,
                "DestroyTime": 0,
                "ExpiryTime": 0,
                "InstanceId": "mqtt-mmgej724",
                "InstanceName": "jehansun-0606",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "MaxSubscriptionPerClient": 30,
                "PayMode": "POSTPAID",
                "Remark": "111",
                "RenewFlag": 0,
                "SkuCode": "basic_1k",
                "TopicNum": 1,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            },
            {
                "AuthorizationPolicyLimit": 10,
                "ClientNumLimit": 100,
                "CreateTime": 1717663172,
                "DestroyTime": 0,
                "ExpiryTime": 0,
                "InstanceId": "mqtt-79opob7m",
                "InstanceName": "jehansun-0628-modify",
                "InstanceStatus": "RUNNING",
                "InstanceType": "BASIC",
                "MaxSubscriptionPerClient": 30,
                "PayMode": "POSTPAID",
                "Remark": "111",
                "RenewFlag": 0,
                "SkuCode": "basic_1k",
                "TopicNum": 1,
                "TopicNumLimit": 25,
                "TpsLimit": 1000,
                "Version": "1"
            }
        ],
        "RequestId": "bf1e881a-f1bc-45bf-b276-4a05b920fbeb",
        "TotalCount": 5
    }
}
```

