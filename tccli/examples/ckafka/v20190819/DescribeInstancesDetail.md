**Example 1: 获取实例列表详情**



Input: 

```
tccli ckafka DescribeInstancesDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "84b84177-c5aa-4fa9-aae0-14618af7d251",
        "Result": {
            "InstanceList": [
                {
                    "Bandwidth": 800,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1732245392,
                    "Cvm": 1,
                    "DiskSize": 1000,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 1734837392,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "",
                    "InstanceId": "ckafka-wdvgwwx2",
                    "InstanceName": "test-public-network",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 1200,
                    "MaxTopicNumber": 600,
                    "PartitionNumber": 60,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_PREPAID",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 0,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 6,
                    "Version": "2.8.1",
                    "Vip": "10.0.1.17",
                    "VipList": [
                        {
                            "Vip": "10.0.1.17",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": [
                        100006,
                        100007
                    ]
                },
                {
                    "Bandwidth": 19200,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1732086196,
                    "Cvm": 1,
                    "DiskSize": -1,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 0,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "",
                    "InstanceId": "ckafka-vv7wpp93",
                    "InstanceName": "wenbingshen-测试",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 5000,
                    "MaxTopicNumber": 2500,
                    "PartitionNumber": 46,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 0,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 3,
                    "Version": "2.8.1",
                    "Vip": "10.0.1.31",
                    "VipList": [
                        {
                            "Vip": "10.0.1.31",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": [
                        100006,
                        100007
                    ]
                },
                {
                    "Bandwidth": 160,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1731479434,
                    "Cvm": 1,
                    "DiskSize": 200,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 1734071434,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "",
                    "InstanceId": "ckafka-bzmjpp4z",
                    "InstanceName": "Reserved_hdq_0.6_2.8",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 400,
                    "MaxTopicNumber": 200,
                    "PartitionNumber": 18,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_PREPAID",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 0,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 3,
                    "Version": "2.8.1",
                    "Vip": "10.0.1.3",
                    "VipList": [
                        {
                            "Vip": "10.0.1.3",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": []
                },
                {
                    "Bandwidth": 160,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1724071025,
                    "Cvm": 1,
                    "DiskSize": 200,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 1734611825,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "",
                    "InstanceId": "ckafka-mon24787",
                    "InstanceName": "carwyn-测试 勿删",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 400,
                    "MaxTopicNumber": 200,
                    "PartitionNumber": 26,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_PREPAID",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 1,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 5,
                    "Version": "1.1.1",
                    "Vip": "10.0.1.29",
                    "VipList": [
                        {
                            "Vip": "10.0.1.29",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": [
                        100006,
                        100007
                    ]
                },
                {
                    "Bandwidth": 1600,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1722481364,
                    "Cvm": 1,
                    "DiskSize": 1000,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 0,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "",
                    "InstanceId": "ckafka-5k7va2bv",
                    "InstanceName": "shilinlu-test-勿动",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 1400,
                    "MaxTopicNumber": 700,
                    "PartitionNumber": 72,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 0,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 5,
                    "Version": "2.8.1",
                    "Vip": "10.0.1.40",
                    "VipList": [
                        {
                            "Vip": "10.0.1.40",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": [
                        100006,
                        100007
                    ]
                },
                {
                    "Bandwidth": 3200,
                    "ClusterType": "CLOUD_CVM",
                    "CreateTime": 1716451701,
                    "Cvm": 1,
                    "DiskSize": 3000,
                    "DiskType": "CLOUD_SSD",
                    "ExpireTime": 0,
                    "Features": [
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "healthy",
                    "InstanceId": "ckafka-na37x9qa",
                    "InstanceName": "shilinlu-exporter 测试",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 2000,
                    "MaxTopicNumber": 1000,
                    "PartitionNumber": 22,
                    "PublicNetwork": 3,
                    "PublicNetworkChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "RebalanceTime": "0000-00-00 00:00:00",
                    "RenewFlag": 0,
                    "Status": 1,
                    "SubnetId": "subnet-5rhipsse",
                    "Tags": [],
                    "TopicNum": 2,
                    "Version": "2.4.1",
                    "Vip": "10.0.1.25",
                    "VipList": [
                        {
                            "Vip": "10.0.1.25",
                            "Vport": "9092"
                        }
                    ],
                    "VpcId": "vpc-ks7w9y0b",
                    "Vport": "9092",
                    "ZoneId": 100006,
                    "ZoneIds": []
                },
                {
                    "Bandwidth": 1200,
                    "ClusterType": "CLOUD_EKS_TSE",
                    "CreateTime": 1667461825,
                    "Cvm": 1,
                    "DiskSize": 1000,
                    "DiskType": "CLOUD_BASIC",
                    "ExpireTime": 1735890625,
                    "Features": [
                        "CLOUD_EKS_TSE",
                        "CLOUD_EKS_CROS_ZONE",
                        "FEATURE_SASL_SCRAM"
                    ],
                    "Healthy": 1,
                    "HealthyMessage": "healthy",
                    "InstanceId": "ckafka-pkwxedpq",
                    "InstanceName": "【勿删-不要再新建公网域名了，会产生安全工单】spock-test",
                    "InstanceType": "profession",
                    "IsInternal": 0,
                    "MaxPartitionNumber": 1200,
                    "MaxTopicNumber": 600,
                    "PartitionNumber": 1026,
                    "PublicNetwork": 6,
                    "PublicNetworkChargeType": "BANDWIDTH_PREPAID",
                    "RebalanceTime": "2023-07-04 10:30:58",
                    "RenewFlag": 1,
                    "Status": 1,
                    "SubnetId": "subnet-kg07707y",
                    "Tags": [
                        {
                            "TagKey": "Application",
                            "TagValue": "underlay-domain"
                        },
                        {
                            "TagKey": "tagkey",
                            "TagValue": "555555"
                        }
                    ],
                    "TopicNum": 61,
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
            ],
            "TotalCount": 7
        }
    }
}
```

