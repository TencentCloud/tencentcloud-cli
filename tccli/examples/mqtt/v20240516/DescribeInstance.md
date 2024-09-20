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
    "Error": null,
    "RequestId": null,
    "Response": {
        "AuthorizationPolicyLimit": 10,
        "AutomaticActivation": false,
        "ClientNumLimit": 1000,
        "CreatedTime": 1722572792,
        "DestroyTime": 0,
        "DeviceCertificateProvisionType": "MANUAL",
        "ExpiryTime": 0,
        "InstanceId": "mqtt-bg8k8v8o",
        "InstanceName": "jehansun-0802",
        "InstanceStatus": "RUNNING",
        "InstanceType": "BASIC",
        "MaxSubscriptionPerClient": 30,
        "PayMode": "POSTPAID",
        "Remark": "",
        "RenewFlag": 1,
        "RequestId": "3e180cf0-ddb8-4a0b-8855-c69c5dc02f35",
        "SkuCode": "basic_1k",
        "TopicNum": 0,
        "TopicNumLimit": 100,
        "TpsLimit": 1000,
        "X509Mode": "TLS"
    }
}
```

