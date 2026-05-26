**Example 1: 查询实例详情**



Input: 

```
tccli tdmysql DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql3-a5952a76
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
        "ColumnarNodeCpu": 0,
        "ColumnarNodeDisk": 0,
        "ColumnarNodeMem": 0,
        "ColumnarNodeNum": 0,
        "ColumnarNodeSpecCode": "",
        "ColumnarNodeStorageType": "",
        "ColumnarVip": "",
        "ColumnarVport": 0,
        "CreateTime": "2026-04-20 21:18:35",
        "CreateVersion": "21.6.2.0.permanent.1192.ssl",
        "Disk": 100,
        "DiskUsage": 19,
        "DumperVip": "",
        "DumperVport": 0,
        "ExpireAt": "0001-01-01 00:00:00",
        "FullReplications": 3,
        "InitParams": [
            {
                "Param": "lower_case_table_names",
                "Value": "1"
            }
        ],
        "InstanceCategory": 0,
        "InstanceId": "tdsql3-446540ae",
        "InstanceMode": "normal",
        "InstanceName": "test003",
        "InstanceType": "hybrid",
        "IsSupportColumnar": true,
        "IsSwitchFullReplicationsEnable": false,
        "IsolatedAt": "0001-01-01 00:00:00",
        "MaintenanceWindow": {
            "Duration": 3600,
            "StartTime": 10800,
            "WeekDays": [
                "Monday"
            ]
        },
        "Node": [
            {
                "BinlogInfo": [],
                "Cpu": 1,
                "DataDisk": 100,
                "Host": "",
                "IP": "10.0.70.65",
                "Mem": 2,
                "NodeId": "node-tdsql3-446540ae-001",
                "Port": 6008,
                "Type": "hybridnode",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "PayMode": "postPay",
        "Region": "ap-guangzhou",
        "RenewFlag": 0,
        "Replications": 3,
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
        "SubnetId": "subnet-30tyayxk",
        "TemplateId": "",
        "TemplateName": "",
        "TimingModifyInstanceFlag": 1,
        "UpdateTime": "2026-04-23 12:13:32",
        "Vip": "10.31.16.52",
        "VpcId": "vpc-o7ssr1vx",
        "Vport": 3306,
        "Zone": "ap-guangzhou-7",
        "Zones": [
            "ap-guangzhou-7"
        ],
        "RequestId": "27f36bdc-e23b-4b75-aa7c-4a4da0e836c4"
    }
}
```

