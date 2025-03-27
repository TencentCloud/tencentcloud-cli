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
    "RequestId": null,
    "Response": {
        "RequestId": "33a9cba9-f885-47aa-8235-8bdcbd9c90bf",
        "TotalCount": 2,
        "Data": [
            {
                "InstanceId": "mqtt-zxjwkr98",
                "InstanceName": "mqtt-instance",
                "Version": "1",
                "InstanceType": "PRO",
                "InstanceStatus": "RUNNING",
                "PayMode": "POSTPAID",
                "ExpiryTime": 0,
                "Remark": "",
                "TopicNum": 1,
                "SkuCode": "pro_6k_1",
                "TpsLimit": 6000,
                "CreateTime": 1741832627,
                "MaxSubscriptionPerClient": 30,
                "MaxSubscription": 180000,
                "AuthorizationPolicyLimit": 20,
                "ClientNumLimit": 6000,
                "MaxCaNum": 20,
                "RenewFlag": 1,
                "DestroyTime": 0,
                "TopicNumLimit": 300
            },
            {
                "InstanceId": "mqtt-w45zn79z",
                "InstanceName": "mqtt-1226",
                "Version": "1",
                "InstanceType": "PRO",
                "InstanceStatus": "RUNNING",
                "PayMode": "PREPAID",
                "ExpiryTime": 1742972038844,
                "Remark": "",
                "TopicNum": 2,
                "SkuCode": "pro_10k_1",
                "TpsLimit": 10000,
                "CreateTime": 1735196039,
                "MaxSubscriptionPerClient": 30,
                "MaxSubscription": 300000,
                "AuthorizationPolicyLimit": 20,
                "ClientNumLimit": 10000,
                "MaxCaNum": 20,
                "RenewFlag": 1,
                "DestroyTime": 0,
                "TopicNumLimit": 300
            }
        ]
    },
    "Error": null
}
```

