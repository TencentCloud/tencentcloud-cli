**Example 1: 示例**



Input: 

```
tccli mqtt DescribeInstance --cli-unfold-argument  \
    --InstanceId mqtt-vv39gdgx
```

Output: 
```
{
    "Response": {
        "AuthorizationPolicy": true,
        "AuthorizationPolicyLimit": 20,
        "AutoSubscriptionPolicyLimit": 10,
        "AutomaticActivation": true,
        "BlockRuleLimit": 10,
        "ClientNumLimit": 2000,
        "CreatedTime": 1779417260,
        "DeleteProtect": false,
        "DestroyTime": 0,
        "DeviceCertificateProvisionType": "API",
        "EventDialect": "V3",
        "ExpiryTime": 1782095659578,
        "HashMessagePolicy": "TOPIC_NAME",
        "InstanceId": "mqtt-vv39gdgx",
        "InstanceName": "********-0522",
        "InstanceStatus": "RUNNING",
        "InstanceType": "PRO",
        "MaxCaNum": 20,
        "MaxSubscription": 60000,
        "MaxSubscriptionPerClient": 30,
        "MaxTopicFilterPerAutoSubscriptionPolicy": 20,
        "MaxTopicFilterPerSharedSubscriptionGroup": 10,
        "MessageEnrichmentRuleLimit": 10,
        "MessageRate": -1,
        "PayMode": "PREPAID",
        "RegistrationCode": "01d6bc37-***********e4d-52571cac864d",
        "Remark": "",
        "RenewFlag": 1,
        "ServerCertLimit": 3,
        "SharedSubscriptionGroupLimit": 20,
        "SkuCode": "pro_2k_1",
        "TopicNum": 0,
        "TopicNumLimit": 300,
        "TopicPrefixSlashLimit": 2,
        "TpsLimit": 2000,
        "TransportLayerSecurity": "TLSv1.3,TLSv1.2,TLSv1.1,TLSv1",
        "TrustedCaLimit": 3,
        "UseDefaultServerCert": true,
        "X509Mode": "BYOC",
        "RequestId": "13264181-6610-46e1-9971-293cea0b7227"
    }
}
```

