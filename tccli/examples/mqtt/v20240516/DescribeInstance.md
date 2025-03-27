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
        "SkuCode": "pro_6k_1",
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

