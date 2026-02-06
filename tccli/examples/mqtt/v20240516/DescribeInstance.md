**Example 1: 示例**



Input: 

```
tccli mqtt DescribeInstance --cli-unfold-argument  \
    --InstanceId mqtt-7peanr83
```

Output: 
```
{
    "Response": {
        "AuthorizationPolicy": false,
        "AuthorizationPolicyLimit": 20,
        "AutoSubscriptionPolicyLimit": 10,
        "AutomaticActivation": true,
        "ClientNumLimit": 4000,
        "CreatedTime": 1756879989,
        "DestroyTime": 0,
        "DeviceCertificateProvisionType": "API",
        "ExpiryTime": 1759471988911,
        "InstanceId": "mqtt-7peanr83",
        "InstanceName": "instance-1",
        "InstanceStatus": "RUNNING",
        "InstanceType": "PRO",
        "MaxCaNum": 20,
        "MaxSubscription": 120000,
        "MaxSubscriptionPerClient": 30,
        "MaxTopicFilterPerAutoSubscriptionPolicy": 20,
        "MaxTopicFilterPerSharedSubscriptionGroup": 10,
        "MessageRate": -1,
        "PayMode": "PREPAID",
        "RegistrationCode": "client-test",
        "Remark": "",
        "RenewFlag": 1,
        "ServerCertLimit": 3,
        "SharedSubscriptionGroupLimit": 20,
        "SkuCode": "pro_2k_2",
        "TopicNum": 0,
        "TopicNumLimit": 300,
        "TopicPrefixSlashLimit": 2,
        "TpsLimit": 2000,
        "TransportLayerSecurity": "TLSv1.3,TLSv1.2,TLSv1.1,TLSv1",
        "TrustedCaLimit": 3,
        "UseDefaultServerCert": true,
        "X509Mode": "BYOC",
        "RequestId": "8a95a551-ca77-45f6-aa00-77a090cac898"
    }
}
```

