**Example 1: 示例**



Input: 

```
tccli mqtt DescribeInstance --cli-unfold-argument  \
    --InstanceId mqtt-3ja5wo5b
```

Output: 
```
{
    "Response": {
        "AuthorizationPolicy": true,
        "AuthorizationPolicyLimit": 10,
        "AutoSubscriptionPolicyLimit": 10,
        "AutomaticActivation": false,
        "BlockRuleLimit": 5,
        "ClientNumLimit": 2000,
        "CreatedTime": 1772163943,
        "DestroyTime": 0,
        "DeviceCertificateProvisionType": "API",
        "ExpiryTime": 0,
        "InstanceId": "mqtt-3ja5wo5b",
        "InstanceName": "mqtt-shared-test3",
        "InstanceStatus": "RUNNING",
        "InstanceType": "BASIC",
        "MaxCaNum": 20,
        "MaxSubscription": 60000,
        "MaxSubscriptionPerClient": 30,
        "MaxTopicFilterPerAutoSubscriptionPolicy": 5,
        "MaxTopicFilterPerSharedSubscriptionGroup": 10,
        "MessageEnrichmentRuleLimit": 10,
        "MessageRate": -1,
        "PayMode": "POSTPAID",
        "RegistrationCode": "",
        "Remark": "",
        "RenewFlag": 1,
        "ServerCertLimit": 3,
        "SharedSubscriptionGroupLimit": 20,
        "SkuCode": "basic_2k",
        "TopicNum": 0,
        "TopicNumLimit": 20,
        "TopicPrefixSlashLimit": 2,
        "TpsLimit": 2000,
        "TransportLayerSecurity": "TLSv1.3,TLSv1.2,TLSv1.1,TLSv1",
        "TrustedCaLimit": 3,
        "UseDefaultServerCert": true,
        "X509Mode": "TLS",
        "RequestId": "2202b107-4def-4fa4-a487-0499c77620db"
    }
}
```

