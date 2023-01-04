**Example 1: 创建询价**



Input: 

```
tccli emr InquiryPriceCreateInstance --cli-unfold-argument  \
    --ResourceSpec.MasterResourceSpec.StorageType 5 \
    --ResourceSpec.MasterResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.MasterResourceSpec.Cpu 4 \
    --ResourceSpec.MasterResourceSpec.DiskSize 100 \
    --ResourceSpec.MasterResourceSpec.MemSize 16384 \
    --ResourceSpec.MasterResourceSpec.RootSize 100 \
    --ResourceSpec.MasterResourceSpec.Spec CVM.S3 \
    --ResourceSpec.CoreCount 2 \
    --ResourceSpec.CoreResourceSpec.StorageType 5 \
    --ResourceSpec.CoreResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.CoreResourceSpec.Cpu 4 \
    --ResourceSpec.CoreResourceSpec.DiskSize 100 \
    --ResourceSpec.CoreResourceSpec.MemSize 16384 \
    --ResourceSpec.CoreResourceSpec.RootSize 100 \
    --ResourceSpec.CoreResourceSpec.Spec CVM.S3 \
    --ResourceSpec.MasterCount 1 \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-3 \
    --SupportHA 0 \
    --TimeSpan 3600 \
    --VPCSettings.SubnetId subnet-jhgsahx0 \
    --VPCSettings.VpcId vpc-ezt5qmqz \
    --PayMode 0 \
    --Currency CNY \
    --TimeUnit s \
    --ProductId 2 \
    --Software zookeeper-3.4.9 hadoop-2.7.3 knox-1.2.0 hive-2.3.2
```

Output: 
```
{
    "Response": {
        "RequestId": "f329b63c-7cec-41f3-91ae-500cbf86b9eb",
        "TimeSpan": 3600,
        "TimeUnit": "s",
        "DiscountCost": 25,
        "OriginalCost": 25,
        "PriceList": [
            {
                "NodeDetailPrice": [
                    {
                        "NodeType": "task",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 1,
                                "InstanceType": "rootDisk",
                                "Policy": 10,
                                "Price": 0.12,
                                "RealCost": 0.12,
                                "RealTotalCost": 0.12
                            },
                            {
                                "GoodsNum": 1,
                                "InstanceType": "node",
                                "Policy": 10,
                                "Price": 2.16,
                                "RealCost": 2.16,
                                "RealTotalCost": 2.16
                            },
                            {
                                "GoodsNum": 1,
                                "InstanceType": "dataDisk",
                                "Policy": 10,
                                "Price": 0.5,
                                "RealCost": 0.5,
                                "RealTotalCost": 0.5
                            }
                        ]
                    },
                    {
                        "NodeType": "master",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 2,
                                "InstanceType": "rootDisk",
                                "Policy": 10,
                                "Price": 0.12,
                                "RealCost": 0.12,
                                "RealTotalCost": 0.25
                            },
                            {
                                "GoodsNum": 2,
                                "InstanceType": "node",
                                "Policy": 10,
                                "Price": 2.16,
                                "RealCost": 2.16,
                                "RealTotalCost": 4.31
                            },
                            {
                                "GoodsNum": 2,
                                "InstanceType": "dataDisk",
                                "Policy": 10,
                                "Price": 0.5,
                                "RealCost": 0.5,
                                "RealTotalCost": 1
                            }
                        ]
                    },
                    {
                        "NodeType": "core",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 3,
                                "InstanceType": "rootDisk",
                                "Policy": 10,
                                "Price": 0.12,
                                "RealCost": 0.12,
                                "RealTotalCost": 0.37
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "node",
                                "Policy": 10,
                                "Price": 2.15,
                                "RealCost": 2.15,
                                "RealTotalCost": 6.46
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "dataDisk",
                                "Policy": 10,
                                "Price": 0.5,
                                "RealCost": 0.5,
                                "RealTotalCost": 1.5
                            }
                        ]
                    },
                    {
                        "NodeType": "common",
                        "PartDetailPrice": [
                            {
                                "GoodsNum": 3,
                                "InstanceType": "rootDisk",
                                "Policy": 10,
                                "Price": 0.12,
                                "RealCost": 0.12,
                                "RealTotalCost": 0.37
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "node",
                                "Policy": 10,
                                "Price": 2.15,
                                "RealCost": 2.15,
                                "RealTotalCost": 6.46
                            },
                            {
                                "GoodsNum": 3,
                                "InstanceType": "dataDisk",
                                "Policy": 10,
                                "Price": 0.5,
                                "RealCost": 0.5,
                                "RealTotalCost": 1.5
                            }
                        ]
                    }
                ],
                "ZoneId": "100003"
            }
        ]
    }
}
```

