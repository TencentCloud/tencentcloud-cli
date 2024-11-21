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
        "ClusterList": [
            {
                "AddTime": "2024-11-05 20:39:44",
                "AlarmInfo": "",
                "AliasInfo": "eyJjb21tb24iOiJjb21tb24iLCJjb3JlIjoiY29yZSIsIm1hc3RlciI6Im1hc3RlciIsInRhc2siOiJ0YXNrIn0=",
                "AppId": 1334143,
                "ChargeType": 0,
                "ClusterExternalServiceInfo": null,
                "ClusterId": "emr-hvijzo6n",
                "ClusterName": "odinlli_test_1105",
                "ClusterTitle": "集群运行中",
                "Config": {
                    "ApplicationRole": "",
                    "CbsEncrypt": 0,
                    "ChargeType": 0,
                    "ComNodeSize": 0,
                    "ComResource": {
                        "Cpu": 0,
                        "DiskSize": 0,
                        "DiskType": "",
                        "InstanceType": "",
                        "MemSize": 0,
                        "RootSize": 0,
                        "Spec": "",
                        "SpecName": "",
                        "StorageType": 0
                    },
                    "CoreNodeSize": 2,
                    "CoreResource": {
                        "Cpu": 4,
                        "DiskSize": 200,
                        "DiskType": "CLOUD_SSD",
                        "InstanceType": "",
                        "MemSize": 8192,
                        "RootSize": 70,
                        "Spec": "CVM.S5",
                        "SpecName": "EMR标准型S5",
                        "StorageType": 4
                    },
                    "MasterNodeSize": 1,
                    "MasterResource": {
                        "Cpu": 8,
                        "DiskSize": 200,
                        "DiskType": "CLOUD_SSD",
                        "InstanceType": "",
                        "MemSize": 16384,
                        "RootSize": 70,
                        "Spec": "CVM.S5",
                        "SpecName": "EMR标准型S5",
                        "StorageType": 4
                    },
                    "OnCos": false,
                    "PublicKeyId": "",
                    "RouterNodeSize": 0,
                    "SecurityGroup": "sg-jfluz1nt",
                    "SecurityGroups": [
                        "sg-jfluz1nt"
                    ],
                    "SecurityOn": false,
                    "SoftInfo": [
                        "hdfs-3.2.2",
                        "yarn-3.2.2",
                        "zookeeper-3.6.3",
                        "openldap-2.4.44",
                        "knox-1.6.1"
                    ],
                    "SupportHA": false,
                    "TaskNodeSize": 0,
                    "TaskResource": {
                        "Cpu": 0,
                        "DiskSize": 0,
                        "DiskType": "",
                        "InstanceType": "",
                        "MemSize": 0,
                        "RootSize": 0,
                        "Spec": "",
                        "SpecName": "",
                        "StorageType": 0
                    }
                },
                "ConfigDetail": {
                    "ApplicationRole": "",
                    "CbsEncrypt": 0,
                    "ChargeType": 0,
                    "ComNodeSize": 0,
                    "ComResource": {
                        "Cpu": 0,
                        "DiskSize": 0,
                        "DiskType": "",
                        "InstanceType": "",
                        "MemSize": 0,
                        "RootSize": 0,
                        "Spec": "",
                        "SpecName": "",
                        "StorageType": 0
                    },
                    "CoreNodeSize": 2,
                    "CoreResource": {
                        "Cpu": 4,
                        "DiskSize": 200,
                        "DiskType": "CLOUD_SSD",
                        "InstanceType": "",
                        "MemSize": 8192,
                        "RootSize": 70,
                        "Spec": "CVM.S5",
                        "SpecName": "EMR标准型S5",
                        "StorageType": 4
                    },
                    "MasterNodeSize": 1,
                    "MasterResource": {
                        "Cpu": 8,
                        "DiskSize": 200,
                        "DiskType": "CLOUD_SSD",
                        "InstanceType": "",
                        "MemSize": 16384,
                        "RootSize": 70,
                        "Spec": "CVM.S5",
                        "SpecName": "EMR标准型S5",
                        "StorageType": 4
                    },
                    "OnCos": false,
                    "PublicKeyId": "",
                    "RouterNodeSize": 0,
                    "SecurityGroup": "sg-jfluz1nt",
                    "SecurityGroups": [
                        "sg-jfluz1nt"
                    ],
                    "SecurityOn": false,
                    "SoftInfo": [
                        "hdfs-3.2.2",
                        "yarn-3.2.2",
                        "zookeeper-3.6.3",
                        "openldap-2.4.44",
                        "knox-1.6.1"
                    ],
                    "SupportHA": false,
                    "TaskNodeSize": 0,
                    "TaskResource": {
                        "Cpu": 0,
                        "DiskSize": 0,
                        "DiskType": "",
                        "InstanceType": "",
                        "MemSize": 0,
                        "RootSize": 0,
                        "Spec": "",
                        "SpecName": "",
                        "StorageType": 0
                    }
                },
                "DisplayName": "默认场景",
                "EmrVersion": "EMR-V3.5.0",
                "Ftitle": "集群运行中",
                "HiveMetaDb": "",
                "Id": 1113,
                "IsCvmReplace": false,
                "IsMultiZoneCluster": false,
                "IsTradeCluster": 0,
                "IsWoodpeckerCluster": 1,
                "MasterIp": "0.0.0.0",
                "MetaDb": "",
                "ProductId": 44,
                "ProjectId": 0,
                "RegionId": 1,
                "ResourceOrderId": 0,
                "RunTime": "0天0小时32分钟20秒",
                "SceneEmrVersion": "EMR-V3.5.0",
                "SceneName": "Hadoop-Default",
                "SceneServiceClass": "Hadoop",
                "ServiceClass": "HADOOP",
                "Status": 2,
                "SubnetId": 6131299,
                "SubnetName": "vigo-subnet",
                "Tags": [],
                "TopologyInfoList": [
                    {
                        "NodeInfoList": [
                            {
                                "NodeSize": 2,
                                "NodeType": "Core"
                            },
                            {
                                "NodeSize": 0,
                                "NodeType": "Task"
                            },
                            {
                                "NodeSize": 0,
                                "NodeType": "Router"
                            },
                            {
                                "NodeSize": 0,
                                "NodeType": "Common"
                            },
                            {
                                "NodeSize": 1,
                                "NodeType": "Master"
                            }
                        ],
                        "SubnetInfoList": [
                            {
                                "SubnetId": "subnet-ax8z9f1u",
                                "SubnetName": "vigo-subnet"
                            }
                        ],
                        "Zone": "ap-guangzhou-3",
                        "ZoneId": 100003
                    }
                ],
                "TradeVersion": 1,
                "Uin": "0000000",
                "UniqSubnetId": "subnet-ax8z9f1u",
                "UniqVpcId": "vpc-r2g15ki3",
                "VpcId": 10421586,
                "VpcName": "vigo-vpc",
                "Zone": "ap-guangzhou-3",
                "ZoneId": 100003
            }
        ],
        "RequestId": "7fd5fb20-1b1f-4425-ad13-1763f0f7f8dc",
        "TagKeys": [],
        "TotalCnt": 1
    }
}
```

