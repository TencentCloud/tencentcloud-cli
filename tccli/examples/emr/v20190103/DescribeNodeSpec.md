**Example 1: 查询机型配置**



Input: 

```
tccli emr DescribeNodeSpec --cli-unfold-argument  \
    --ZoneId 100003 \
    --CvmPayMode 0 \
    --NodeType Core \
    --TradeType 1 \
    --ProductId 20 \
    --SceneName Hadoop-Default \
    --ResourceBaseType ComputeResource
```

Output: 
```
{
    "Response": {
        "Architectures": [
            {
                "Architecture": "X86 Computing",
                "ArchitectureName": "X86计算",
                "InstanceFamilies": [
                    "S2"
                ],
                "Order": 1
            }
        ],
        "NodeSpecs": [
            {
                "CmnTypes": [],
                "NodeName": "Core 节点",
                "NodeType": "Core",
                "Types": [
                    {
                        "InstanceFamilies": [
                            {
                                "FamilyName": "标准型S2",
                                "InstanceFamily": "S2",
                                "InstanceTypes": [
                                    {
                                        "Cpu": 4,
                                        "CpuType": "Intel Xeon E5-2680 v4",
                                        "DataDisk": [
                                            {
                                                "Count": 1,
                                                "DefaultDiskSize": 100,
                                                "DiskType": "CLOUD_BSSD",
                                                "IsSpecialDisk": false,
                                                "Name": "通用型SSD云硬盘"
                                            }
                                        ],
                                        "FamilyName": "",
                                        "GpuDesc": "",
                                        "GpuNum": 0,
                                        "GpuResourceKey": "",
                                        "InstanceFamily": "",
                                        "InstanceType": "S2.LARGE8",
                                        "IsGpuInstance": true,
                                        "LocalDataDisk": [],
                                        "Memory": 8,
                                        "NeedHpcClusterId": false,
                                        "NodeName": "Core 节点",
                                        "NodeType": "Core",
                                        "Num": 580,
                                        "Order": 0,
                                        "OriginPrice": 1.44,
                                        "PrepaidUnderwritePeriods": null,
                                        "QuotaNum": 899992,
                                        "QuotaUnit": "VCPU",
                                        "Remark": "Enough",
                                        "SellOutReason": "",
                                        "SoldOutReason": "",
                                        "SystemDisk": [
                                            {
                                                "Count": 1,
                                                "DefaultDiskSize": 70,
                                                "DiskType": "CLOUD_BSSD",
                                                "IsSpecialDisk": false,
                                                "Name": "通用型SSD云硬盘"
                                            }
                                        ],
                                        "Type": "",
                                        "TypeName": ""
                                    }
                                ],
                                "Order": 14
                            }
                        ],
                        "Order": 1,
                        "Type": "S",
                        "TypeName": "标准型"
                    }
                ]
            }
        ],
        "RequestId": "18d59c7d-39de-4fbb-b6c0-2a5d18c09d5e"
    }
}
```

