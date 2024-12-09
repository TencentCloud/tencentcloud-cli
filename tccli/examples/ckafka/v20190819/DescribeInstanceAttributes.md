**Example 1: 获取实例属性**



Input: 

```
tccli ckafka DescribeInstanceAttributes --cli-unfold-argument  \
    --InstanceId ckafka-pkwxedpq
```

Output: 
```
{
    "Response": {
        "RequestId": "dc67ed1b-3ada-4dad-9c5e-dc2a3619558e",
        "Result": {
            "Bandwidth": 1200,
            "ClusterType": "CLOUD_EKS_TSE",
            "Config": {
                "AutoCreateTopicsEnable": true,
                "DefaultNumPartitions": 10,
                "DefaultReplicationFactor": 2
            },
            "CreateTime": 1667461825,
            "CreatedPartitions": 1026,
            "CreatedTopics": 61,
            "CustomCertId": "certid",
            "Cvm": 1,
            "DeleteRouteTimestamp": "",
            "DiskSize": 1000,
            "DynamicDiskConfig": {
                "DiskQuotaPercentage": 75,
                "Enable": 1,
                "MaxDiskSpace": 500000,
                "StepForwardPercentage": 10
            },
            "ElasticFloatBandwidth": 480,
            "ExpireTime": 1735890625,
            "Features": [
                "FEATURE_SUBNET_ACL",
                "FEATURE_SASL_SSL",
                "FEATURE_MULIT_SASL_PLAINTEXT",
                "FEATURE_TOPIC_QUOTA",
                "FEATURE_SASL_SCRAM_512",
                "CLOUD_EKS_TSE",
                "CLOUD_EKS_CROS_ZONE",
                "FEATURE_SASL_SCRAM"
            ],
            "FreePartitionNumber": 1200,
            "Healthy": 1,
            "HealthyMessage": "healthy",
            "InstanceChargeType": "PREPAID",
            "InstanceId": "ckafka-pkwxedpq",
            "InstanceName": "【勿删-不要再新建公网域名了，会产生安全工单】spock-test",
            "InstanceType": "profession",
            "MaxConnection": 10000,
            "MaxGroupNum": 200,
            "MsgRetentionTime": 2880,
            "PublicNetwork": 6,
            "RemainderPartitions": 174,
            "RemainderTopics": 539,
            "RemainingPartitions": 174,
            "RemainingTopics": 539,
            "RetentionTimeConfig": {
                "BottomRetention": 360,
                "DiskQuotaPercentage": 75,
                "Enable": 0,
                "StepForwardPercentage": 10
            },
            "Status": 1,
            "SubnetId": "subnet-kg07707y",
            "Tags": [
                {
                    "TagKey": "Application",
                    "TagValue": "underlay-domain"
                },
                {
                    "TagKey": "key",
                    "TagValue": "555555"
                }
            ],
            "Version": "2.4.1",
            "Vip": "172.16.0.17",
            "VipList": [
                {
                    "Vip": "172.16.0.17",
                    "Vport": "9092"
                }
            ],
            "VpcId": "vpc-apwrtw01",
            "Vport": "9092",
            "ZoneId": 100006,
            "ZoneIds": [
                100006,
                100007
            ]
        }
    }
}
```

