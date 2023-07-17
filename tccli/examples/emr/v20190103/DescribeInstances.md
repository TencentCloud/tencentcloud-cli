**Example 1: 查询实例详情**

查询实例详情

Input: 

```
tccli emr DescribeInstances --cli-unfold-argument  \
    --DisplayStrategy clusterList \
    --ProjectId 0 \
    --Asc 0 \
    --Limit 10 \
    --OrderField clusterid \
    --Offset 0 \
    --InstanceIds emr-p9f700x8
```

Output: 
```
{
    "Response": {
        "TotalCnt": 0,
        "ClusterList": [
            {
                "Id": 0,
                "ClusterId": "abc",
                "Ftitle": "abc",
                "ClusterName": "abc",
                "RegionId": 0,
                "ZoneId": 0,
                "AppId": 0,
                "Uin": "abc",
                "ProjectId": 0,
                "VpcId": 0,
                "SubnetId": 0,
                "Status": 0,
                "AddTime": "abc",
                "RunTime": "abc",
                "Config": {
                    "SoftInfo": [
                        "abc"
                    ],
                    "MasterNodeSize": 0,
                    "CoreNodeSize": 0,
                    "TaskNodeSize": 0,
                    "ComNodeSize": 0,
                    "MasterResource": {
                        "Spec": "abc",
                        "SpecName": "abc",
                        "StorageType": 0,
                        "DiskType": "abc",
                        "RootSize": 0,
                        "MemSize": 0,
                        "Cpu": 0,
                        "DiskSize": 0,
                        "InstanceType": "abc"
                    },
                    "CoreResource": {
                        "Spec": "abc",
                        "SpecName": "abc",
                        "StorageType": 0,
                        "DiskType": "abc",
                        "RootSize": 0,
                        "MemSize": 0,
                        "Cpu": 0,
                        "DiskSize": 0,
                        "InstanceType": "abc"
                    },
                    "TaskResource": {
                        "Spec": "abc",
                        "SpecName": "abc",
                        "StorageType": 0,
                        "DiskType": "abc",
                        "RootSize": 0,
                        "MemSize": 0,
                        "Cpu": 0,
                        "DiskSize": 0,
                        "InstanceType": "abc"
                    },
                    "OnCos": true,
                    "ChargeType": 0,
                    "RouterNodeSize": 0,
                    "SupportHA": true,
                    "SecurityOn": true,
                    "SecurityGroup": "abc",
                    "CbsEncrypt": 0,
                    "ApplicationRole": "abc",
                    "SecurityGroups": [
                        "abc"
                    ],
                    "PublicKeyId": "abc"
                },
                "MasterIp": "abc",
                "EmrVersion": "abc",
                "ChargeType": 0,
                "TradeVersion": 0,
                "ResourceOrderId": 0,
                "IsTradeCluster": 0,
                "AlarmInfo": "abc",
                "IsWoodpeckerCluster": 0,
                "MetaDb": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "HiveMetaDb": "abc",
                "ServiceClass": "abc",
                "AliasInfo": "abc",
                "ProductId": 0,
                "Zone": "abc",
                "SceneName": "abc",
                "SceneServiceClass": "abc",
                "SceneEmrVersion": "abc",
                "DisplayName": "abc",
                "VpcName": "abc",
                "SubnetName": "abc",
                "ClusterExternalServiceInfo": [
                    {
                        "DependType": 0,
                        "Service": "abc",
                        "ClusterId": "abc",
                        "ClusterStatus": 0
                    }
                ],
                "UniqVpcId": "abc",
                "UniqSubnetId": "abc",
                "TopologyInfoList": [
                    {
                        "ZoneId": 0,
                        "Zone": "abc",
                        "SubnetInfoList": [
                            {
                                "SubnetName": "abc",
                                "SubnetId": "abc"
                            }
                        ],
                        "NodeInfoList": [
                            {
                                "NodeType": "abc",
                                "NodeSize": 1
                            }
                        ]
                    }
                ],
                "IsMultiZoneCluster": true,
                "IsCvmReplace": true
            }
        ],
        "TagKeys": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

