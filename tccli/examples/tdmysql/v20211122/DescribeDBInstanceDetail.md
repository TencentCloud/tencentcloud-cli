**Example 1: 查询实例详情**



Input: 

```
tccli tdmysql DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql3-5ff6a8b8
```

Output: 
```
{
    "Response": {
        "AZMode": 1,
        "AnalysisInstanceInfo": {
            "ReplicasNum": 0
        },
        "AnalysisMode": "",
        "AnalysisRelationInfos": [],
        "BinlogStatus": 0,
        "BinlogType": "",
        "CharSet": "utf8mb4",
        "Collation": "utf8mb4_0900_ai_ci",
        "ColumnarNodeCpu": 0,
        "ColumnarNodeDisk": 0,
        "ColumnarNodeMem": 0,
        "ColumnarNodeNum": 0,
        "ColumnarNodeSpecCode": "",
        "ColumnarNodeStorageType": "",
        "ColumnarVip": "",
        "ColumnarVport": 0,
        "CreateTime": "2026-08-14 17:12:30",
        "CreateVersion": "21.6.4.0",
        "Disk": 50,
        "DiskUsage": 8,
        "DumperVip": "",
        "DumperVport": 0,
        "EncryptionEnable": 0,
        "EncryptionKmsRegion": "",
        "ExpireAt": "0001-01-01 00:00:00",
        "FullReplications": 3,
        "InitParams": [
            {
                "Param": "character_set_server",
                "Value": "utf8mb4"
            },
            {
                "Param": "collation_server",
                "Value": "utf8mb4_0900_ai_ci"
            },
            {
                "Param": "lower_case_table_names",
                "Value": "1"
            },
            {
                "Param": "tdstore_enter_readonly_threshold_percent",
                "Value": "99.00"
            }
        ],
        "InstanceCategory": 0,
        "InstanceId": "tdsql3-6m0tk7ovso",
        "InstanceMode": "normal",
        "InstanceName": "tdsql-test-05",
        "InstanceType": "hybrid",
        "IsSupportColumnar": true,
        "IsSwitchFullReplicationsEnable": true,
        "IsolatedAt": "0001-01-01 00:00:00",
        "Node": [
            {
                "BinlogInfo": [],
                "Cpu": 1,
                "DataDisk": 50,
                "Host": "",
                "IP": "10.0.71.213",
                "Mem": 2,
                "NodeId": "node-tdsql3-6m0tk7ovso-001",
                "Port": 6008,
                "Type": "hybridnode",
                "Zone": "ap-guangzhou-7"
            },
            {
                "BinlogInfo": [],
                "Cpu": 1,
                "DataDisk": 50,
                "Host": "",
                "IP": "10.0.70.185",
                "Mem": 2,
                "NodeId": "node-tdsql3-6m0tk7ovso-002",
                "Port": 6008,
                "Type": "hybridnode",
                "Zone": "ap-guangzhou-7"
            },
            {
                "BinlogInfo": [],
                "Cpu": 1,
                "DataDisk": 50,
                "Host": "",
                "IP": "10.0.71.244",
                "Mem": 2,
                "NodeId": "node-tdsql3-6m0tk7ovso-003",
                "Port": 6008,
                "Type": "hybridnode",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "PayMode": "postPay",
        "Region": "ap-guangzhou",
        "RenewFlag": 0,
        "Replications": 3,
        "RequestId": "705378eb-1e06-4206-b5bb-f05b07cd98dc",
        "ResourceTags": [],
        "SQLMode": "MySQL",
        "SpecCode": "1c2g",
        "StandbyFlag": 1,
        "Status": "running",
        "StatusDesc": "运行中",
        "StorageNodeCpu": 1,
        "StorageNodeMem": 2,
        "StorageNodeNum": 3,
        "StorageType": "CLOUD_HSSD",
        "SubnetId": "subnet-2xuqw7eg",
        "TemplateId": "",
        "TemplateName": "",
        "TimingModifyInstanceFlag": 1,
        "UpdateTime": "2026-09-15 14:46:44",
        "Vip": "172.16.17.101",
        "VpcId": "vpc-e0cfcqy3",
        "Vport": 3306,
        "Zone": "ap-guangzhou-7",
        "Zones": [
            "ap-guangzhou-7"
        ]
    }
}
```

