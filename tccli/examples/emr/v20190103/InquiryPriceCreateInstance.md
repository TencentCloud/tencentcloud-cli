**Example 1: 创建集群询价**



Input: 

```
tccli emr InquiryPriceCreateInstance --cli-unfold-argument  \
    --ProductId 53 \
    --PayMode 1 \
    --SupportHA 1 \
    --Software hdfs-3.2.2 yarn-3.2.2 zookeeper-3.6.3 openldap-2.4.44 knox-1.6.1 hive-3.1.3 \
    --TimeUnit m \
    --TimeSpan 1 \
    --SceneName Hadoop-Default \
    --VersionID 1 \
    --MultiZoneSettings.0.Placement.ProjectId 0 \
    --MultiZoneSettings.0.Placement.Zone 100002 \
    --MultiZoneSettings.0.VPCSettings.VpcId vpc-j5tovf55 \
    --MultiZoneSettings.0.VPCSettings.SubnetId  \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.InstanceType S2.2XLARGE16 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.Cpu 4 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.MemSize 1024 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.DiskSize 14321 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.Spec SA5 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.StorageType 1 \
    --MultiZoneSettings.0.ResourceSpec.MasterResourceSpec.DiskType CLOUD_SSD \
    --MultiZoneSettings.0.ResourceSpec.MasterCount 2 \
    --MultiZoneSettings.0.ResourceSpec.CoreResourceSpec.InstanceType SA2.LARGE8 \
    --MultiZoneSettings.0.ResourceSpec.CoreCount 3 \
    --MultiZoneSettings.0.ResourceSpec.CommonResourceSpec.InstanceType S2.MEDIUM4 \
    --MultiZoneSettings.0.ResourceSpec.CommonCount 3 \
    --MultiZoneSettings.0.ResourceSpec.TaskResourceSpec.InstanceType SA2.LARGE8 \
    --MultiZoneSettings.0.ResourceSpec.TaskCount 0 \
    --MetaType EMR_DEFAULT_META \
    --DefaultMetaVersion mysql8 \
    --NeedCdbAudit 0 \
    --Currency CNY
```

Output: 
```
{
    "Response": {
        "DiscountCost": 5680.2,
        "OriginalCost": 5680.2,
        "PriceList": [
            {
                "NodeDetailPrice": [
                    {
                        "NodeType": "Master",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 2,
                                "InstanceType": "节点",
                                "Policy": 10,
                                "Price": 828,
                                "RealCost": 828,
                                "RealTotalCost": 1656
                            },
                            {
                                "GoodsNum": 2,
                                "InstanceType": "系统盘",
                                "Policy": 10,
                                "Price": 70,
                                "RealCost": 70,
                                "RealTotalCost": 140
                            },
                            {
                                "GoodsNum": 2,
                                "InstanceType": "数据盘",
                                "Policy": 10,
                                "Price": 200,
                                "RealCost": 200,
                                "RealTotalCost": 400
                            }
                        ]
                    },
                    {
                        "NodeType": "Common",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 3,
                                "InstanceType": "节点",
                                "Policy": 10,
                                "Price": 207,
                                "RealCost": 207,
                                "RealTotalCost": 621
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "系统盘",
                                "Policy": 10,
                                "Price": 50,
                                "RealCost": 50,
                                "RealTotalCost": 150
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "数据盘",
                                "Policy": 10,
                                "Price": 200,
                                "RealCost": 200,
                                "RealTotalCost": 600
                            }
                        ]
                    },
                    {
                        "NodeType": "Core",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 3,
                                "InstanceType": "节点",
                                "Policy": 10,
                                "Price": 294.4,
                                "RealCost": 294.4,
                                "RealTotalCost": 883.2
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "系统盘",
                                "Policy": 10,
                                "Price": 50,
                                "RealCost": 50,
                                "RealTotalCost": 150
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "数据盘",
                                "Policy": 10,
                                "Price": 200,
                                "RealCost": 200,
                                "RealTotalCost": 600
                            }
                        ]
                    },
                    {
                        "NodeType": "MySQL",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 1,
                                "InstanceType": "MetaDB",
                                "Policy": 10,
                                "Price": 480,
                                "RealCost": 480,
                                "RealTotalCost": 480
                            }
                        ]
                    }
                ],
                "ZoneId": "100002"
            }
        ],
        "RequestId": "f70d3401-e7eb-403e-b769-4df8185e552b",
        "TimeSpan": 1,
        "TimeUnit": "m"
    }
}
```

