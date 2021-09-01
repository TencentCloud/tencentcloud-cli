**Example 1: 查询实例详情**



Input: 

```
tccli emr DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ProjectId 0 \
    --OrderField clusterid \
    --Asc 0 \
    --DisplayStrategy clusterList \
    --InstanceIds emr-p9f700x8
```

Output: 
```
{
    "Response": {
        "ClusterList": [
            {
                "AddTime": "2021-01-20 21:28:05",
                "AlarmInfo": "",
                "AliasInfo": "eyJjb21tb24iOiJjb21tb24iLCJjb3JlIjoiY29yZSIsIm1hc3RlciI6Im1hc3RlciIsInRhc2siOiJ0YXNrIn0=",
                "AppId": 1258469122,
                "ChargeType": 1,
                "ClusterId": "emr-myzhptk6",
                "ClusterName": "ganlu-hdfs-study-一直在用-勿删",
                "Config": {
                    "ApplicationRole": "",
                    "CbsEncrypt": 0,
                    "ChargeType": 1,
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
                        "DiskSize": 100,
                        "DiskType": "CLOUD_PREMIUM",
                        "InstanceType": "",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 5
                    },
                    "MasterNodeSize": 1,
                    "MasterResource": {
                        "Cpu": 4,
                        "DiskSize": 100,
                        "DiskType": "CLOUD_PREMIUM",
                        "InstanceType": "",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 5
                    },
                    "OnCos": false,
                    "RouterNodeSize": 0,
                    "SecurityGroup": "sg-9zhz084e",
                    "SecurityGroups": [
                        "sg-9zhz084e"
                    ],
                    "SecurityOn": false,
                    "SoftInfo": [
                        "zookeeper-3.6.1",
                        "yarn-3.1.2",
                        "hdfs-3.1.2",
                        "knox-1.2.0",
                        "hive-3.1.1",
                        "tez-0.9.2"
                    ],
                    "SupportHA": false,
                    "TaskNodeSize": 2,
                    "TaskResource": {
                        "Cpu": 4,
                        "DiskSize": 100,
                        "DiskType": "CLOUD_PREMIUM",
                        "InstanceType": "",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 5
                    }
                },
                "EmrVersion": "EMR-V3.1.0",
                "Ftitle": "集群安装组件中",
                "HiveMetaDb": "cdb-709c8dh9",
                "Id": 150118,
                "IsTradeCluster": 0,
                "IsWoodpeckerCluster": 1,
                "MasterIp": "170.106.101.90",
                "MetaDb": "cdb-709c8dh9",
                "ProductId": 25,
                "ProjectId": 0,
                "RegionId": 15,
                "ResourceOrderId": 0,
                "RunTime": "146天21小时50分钟30秒",
                "ServiceClass": "HADOOP",
                "Status": 6,
                "SubnetId": 85503,
                "Tags": [],
                "TradeVersion": 1,
                "Uin": "100008965662",
                "VpcId": 848834,
                "Zone": "na-siliconvalley-2",
                "ZoneId": 150002
            }
        ],
        "RequestId": "7ee88474-b29a-45b8-9ecc-595d03c4ef95",
        "TagKeys": [],
        "TotalCnt": 1
    }
}
```

