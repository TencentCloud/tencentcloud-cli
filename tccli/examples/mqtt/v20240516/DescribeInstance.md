**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeInstance --cli-unfold-argument  \
    --InstanceId mqtt-bg8k8v8o
```

Output: 
```
{
    "RequestId": null,
    "Response": {
        "RequestId": "5a2634e3-effd-4380-a9ff-3658ec6c1fdc",
        "InstanceType": "PRO",
        "InstanceStatus": "RUNNING",
        "PayMode": "POSTPAID",
        "RenewFlag": 1,
        "DestroyTime": 0,
        "CreatedTime": 1741832627,
        "TpsLimit": 6000,
        "Remark": "",
        "SkuCode": "pro_10k_1",
        "MaxSubscriptionPerClient": 30,
        "MaxSubscription": 180000,
        "AuthorizationPolicyLimit": 20,
        "ClientNumLimit": 6000,
        "MaxCaNum": 20,
        "DeviceCertificateProvisionType": "JITP",
        "RegistrationCode": "66a00d75-8272-421f-be2a-166e2c2e7813",
        "AutomaticActivation": true,
        "X509Mode": "BYOC",
        "ExpiryTime": 0,
        "TopicNumLimit": 300,
        "InstanceId": "mqtt-zxjwkr98",
        "TopicNum": 1,
        "InstanceName": "mqtt-instance1"
    },
    "Error": null
}
```

**Example 2: 查询MQTT实例详情信息**

查询MQTT实例详情信息

Input: 

```
tccli mqtt DescribeInstance --cli-unfold-argument  \
    --InstanceId mqtt-zj944d74
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "AuthorizationPolicy": true,
        "AuthorizationPolicyLimit": 20,
        "AutoSubscriptionPolicyLimit": 10,
        "AutomaticActivation": false,
        "ClientNumLimit": 6000,
        "CreatedTime": 1736236715,
        "DestroyTime": 0,
        "DeviceCertificateProvisionType": "JITP",
        "ExpiryTime": 0,
        "InstanceId": "mqtt-zj944d74",
        "InstanceName": "seiroli-byoc-test-0107",
        "InstanceStatus": "RUNNING",
        "InstanceType": "PRO",
        "MaxCaNum": 20,
        "MaxSubscription": 180000,
        "MaxSubscriptionPerClient": 30,
        "MaxTopicFilterPerAutoSubscriptionPolicy": 5,
        "MaxTopicFilterPerSharedSubscriptionGroup": 10,
        "PayMode": "POSTPAID",
        "RegistrationCode": "bf2ead84-e9e2-478e-a153-3b6baa9b78b1",
        "Remark": "",
        "RenewFlag": 1,
        "RequestId": "a71557b4-34ca-46b0-ab51-2420bf4555c2",
        "SharedSubscriptionGroupLimit": 20,
        "SkuCode": "pro_6k_1",
        "TopicNum": 2,
        "TopicNumLimit": 300,
        "TpsLimit": 6000,
        "X509Mode": "BYOC"
    }
}
```

