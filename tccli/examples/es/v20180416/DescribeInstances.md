**Example 1: 查询ES集群实例**

根据给定条件查询符合条件的ES集群实例并返回详细信息

Input: 

```
tccli es DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "WebNodeTypeInfo": {
                    "NodeNum": 1,
                    "NodeType": "xx"
                },
                "EsPort": 1,
                "RenewFlag": "xx",
                "Zone": "xx",
                "FrozenNodeNum": 1,
                "FrozenCpuNum": 1,
                "ChargePeriod": 1,
                "IkConfig": {
                    "QQDict": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "UpdateType": "xx",
                    "Stopwords": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "MainDict": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "Synonym": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ]
                },
                "WarmMemSize": 1,
                "DiskType": "xx",
                "EsPublicUrl": "xx",
                "NodeNum": 1,
                "FrozenDiskType": "xx",
                "ColdNodeType": "xx",
                "SubnetUid": "xx",
                "EsVip": "xx",
                "NodeInfoList": [
                    {
                        "LocalDiskInfo": {
                            "LocalDiskType": "xx",
                            "LocalDiskSize": 1,
                            "LocalDiskCount": 1
                        },
                        "NodeType": "xx",
                        "DiskEncrypt": 1,
                        "DiskCount": 1,
                        "DiskType": "xx",
                        "NodeNum": 1,
                        "DiskSize": 1,
                        "Type": "xx"
                    }
                ],
                "EsPublicAcl": {
                    "BlackIpList": [
                        "xx"
                    ],
                    "WhiteIpList": [
                        "xx"
                    ]
                },
                "WarmNodeType": "xx",
                "KibanaPublicAccess": "xx",
                "Status": 1,
                "ColdMemSize": 1,
                "UpdateTime": "xx",
                "EnableHotWarmMode": true,
                "EsPrivateUrl": "xx",
                "EsPrivateDomain": "xx",
                "InstanceId": "xx",
                "FrozenNodeType": "xx",
                "CpuNum": 1,
                "ColdNodeNum": 1,
                "CosBackup": {
                    "IsAutoBackup": true,
                    "BackupTime": "xx"
                },
                "FrozenMemSize": 1,
                "SecurityGroups": [
                    "xx"
                ],
                "SceneType": 0,
                "KibanaPrivateUrl": "xx",
                "InstanceType": 1,
                "ColdDiskSize": 1,
                "EsVersion": "xx",
                "ColdDiskType": "xx",
                "AllowCosBackup": true,
                "Jdk": "xx",
                "VpcUid": "xx",
                "Region": "xx",
                "WarmCpuNum": 1,
                "MultiZoneInfo": [
                    {
                        "SubnetId": "xx",
                        "Zone": "xx"
                    }
                ],
                "LicenseType": "xx",
                "EsConfig": "xx",
                "WarmNodeNum": 1,
                "WarmDiskType": "xx",
                "DiskSize": 1,
                "DeployMode": 1,
                "KibanaNodeInfo": {
                    "KibanaNodeNum": 1,
                    "KibanaNodeCpuNum": 1,
                    "KibanaNodeMemSize": 1,
                    "KibanaNodeDiskType": "xx",
                    "KibanaNodeType": "xx",
                    "KibanaNodeDiskSize": 1
                },
                "MemSize": 1,
                "Protocol": "xx",
                "KibanaPrivateAccess": "xx",
                "InstanceName": "xx",
                "EsAcl": {
                    "BlackIpList": [
                        "xx"
                    ],
                    "WhiteIpList": [
                        "xx"
                    ]
                },
                "ColdCpuNum": 1,
                "MasterNodeInfo": {
                    "MasterNodeMemSize": 1,
                    "MasterNodeDiskType": "xx",
                    "MasterNodeType": "xx",
                    "MasterNodeNum": 1,
                    "MasterNodeDiskSize": 1,
                    "EnableDedicatedMaster": true,
                    "MasterNodeCpuNum": 1
                },
                "NodeType": "xx",
                "PublicAccess": "xx",
                "FrozenDiskSize": 1,
                "SecurityType": 1,
                "Uin": "xx",
                "HealthStatus": 0,
                "EsDomain": "xx",
                "WarmDiskSize": 1,
                "Deadline": "xx",
                "ChargeType": "xx",
                "AppId": 1,
                "KibanaUrl": "xx",
                "CreateTime": "xx",
                "KibanaConfig": "xx",
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            },
            {
                "WebNodeTypeInfo": {
                    "NodeNum": 1,
                    "NodeType": "xx"
                },
                "EsPort": 1,
                "RenewFlag": "xx",
                "Zone": "xx",
                "FrozenNodeNum": 1,
                "FrozenCpuNum": 1,
                "ChargePeriod": 1,
                "ColdDiskType": "xx",
                "WarmMemSize": 1,
                "DiskType": "xx",
                "EsPublicUrl": "xx",
                "NodeNum": 1,
                "SecurityType": 1,
                "SubnetUid": "xx",
                "EsVip": "xx",
                "AllowCosBackup": true,
                "EsPublicAcl": {
                    "BlackIpList": [
                        "xx"
                    ],
                    "WhiteIpList": [
                        "xx"
                    ]
                },
                "WarmNodeType": "xx",
                "KibanaPublicAccess": "xx",
                "Status": 1,
                "ColdMemSize": 1,
                "UpdateTime": "xx",
                "InstanceId": "xx",
                "InstanceName": "xx",
                "WarmDiskSize": 1,
                "CpuNum": 1,
                "ColdNodeNum": 1,
                "CosBackup": {
                    "IsAutoBackup": true,
                    "BackupTime": "xx"
                },
                "SecurityGroups": [
                    "xx"
                ],
                "Deadline": "xx",
                "SceneType": 0,
                "KibanaPrivateUrl": "xx",
                "InstanceType": 1,
                "ColdDiskSize": 1,
                "EsVersion": "xx",
                "IkConfig": {
                    "QQDict": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "UpdateType": "xx",
                    "Stopwords": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "MainDict": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ],
                    "Synonym": [
                        {
                            "Name": "xx",
                            "Key": "xx",
                            "Size": 1
                        }
                    ]
                },
                "PublicAccess": "xx",
                "NodeInfoList": [
                    {
                        "LocalDiskInfo": {
                            "LocalDiskType": "xx",
                            "LocalDiskSize": 1,
                            "LocalDiskCount": 1
                        },
                        "NodeType": "xx",
                        "DiskEncrypt": 1,
                        "DiskCount": 1,
                        "DiskType": "xx",
                        "NodeNum": 1,
                        "DiskSize": 1,
                        "Type": "xx"
                    }
                ],
                "Jdk": "xx",
                "VpcUid": "xx",
                "Region": "xx",
                "AppId": 1,
                "MultiZoneInfo": [
                    {
                        "SubnetId": "xx",
                        "Zone": "xx"
                    }
                ],
                "LicenseType": "xx",
                "EsConfig": "xx",
                "WarmNodeNum": 1,
                "DiskSize": 1,
                "DeployMode": 1,
                "KibanaNodeInfo": {
                    "KibanaNodeNum": 1,
                    "KibanaNodeCpuNum": 1,
                    "KibanaNodeMemSize": 1,
                    "KibanaNodeDiskType": "xx",
                    "KibanaNodeType": "xx",
                    "KibanaNodeDiskSize": 1
                },
                "FrozenMemSize": 1,
                "NodeType": "xx",
                "KibanaPrivateAccess": "xx",
                "FrozenNodeType": "xx",
                "EsAcl": {
                    "BlackIpList": [
                        "xx"
                    ],
                    "WhiteIpList": [
                        "xx"
                    ]
                },
                "ColdCpuNum": 1,
                "EsDomain": "xx",
                "MasterNodeInfo": {
                    "MasterNodeMemSize": 1,
                    "MasterNodeDiskType": "xx",
                    "MasterNodeType": "xx",
                    "MasterNodeNum": 1,
                    "MasterNodeDiskSize": 1,
                    "EnableDedicatedMaster": true,
                    "MasterNodeCpuNum": 1
                },
                "Protocol": "xx",
                "MemSize": 1,
                "FrozenDiskSize": 1,
                "ColdNodeType": "xx",
                "Uin": "xx",
                "WarmDiskType": "xx",
                "FrozenDiskType": "xx",
                "HealthStatus": 0,
                "ChargeType": "xx",
                "WarmCpuNum": 1,
                "KibanaUrl": "xx",
                "CreateTime": "xx",
                "EnableHotWarmMode": true,
                "EsPrivateUrl": "xx",
                "EsPrivateDomain": "xx",
                "KibanaConfig": "xx",
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

