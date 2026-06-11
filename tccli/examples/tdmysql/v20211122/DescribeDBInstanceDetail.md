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
        "ColumnarNodeCpu": 0,
        "ColumnarNodeDisk": 0,
        "ColumnarNodeMem": 0,
        "ColumnarNodeNum": 0,
        "ColumnarNodeSpecCode": "",
        "ColumnarNodeStorageType": "",
        "ColumnarVip": "",
        "ColumnarVport": 0,
        "CreateTime": "2026-05-29 15:31:08",
        "CreateVersion": "21.2.7.0",
        "Disk": 20,
        "DiskUsage": 11,
        "DumperVip": "",
        "DumperVport": 0,
        "ExpireAt": "0001-01-01 00:00:00",
        "FullReplications": 1,
        "InitParams": [
            {
                "Param": "character_set_server",
                "Value": "utf8mb4"
            }
        ],
        "InstanceCategory": 4,
        "InstanceId": "tdsql3-5ff6a8b8",
        "InstanceMode": "enhanced",
        "InstanceName": "21270",
        "InstanceType": "hybrid",
        "IsSupportColumnar": false,
        "IsSwitchFullReplicationsEnable": false,
        "IsolatedAt": "0001-01-01 00:00:00",
        "Node": [
            {
                "BinlogInfo": [],
                "Cpu": 1,
                "DataDisk": 20,
                "Host": "",
                "IP": "21.0.204.79",
                "Mem": 2,
                "NodeId": "node-tdsql3-5ff6a8b8-001",
                "Port": 6008,
                "Type": "hybridnode",
                "Zone": "ap-chengdu-1"
            }
        ],
        "PayMode": "postPay",
        "Region": "ap-chengdu",
        "RenewFlag": 0,
        "Replications": 1,
        "ResourceTags": [],
        "SQLMode": "MySQL",
        "SpecCode": "1c2g",
        "StandbyFlag": 1,
        "Status": "running",
        "StatusDesc": "运行中",
        "StorageNodeCpu": 1,
        "StorageNodeMem": 2,
        "StorageNodeNum": 1,
        "StorageType": "CLOUD_HSSD",
        "SubnetId": "subnet-dz7wfk4r",
        "TemplateId": "",
        "TemplateName": "",
        "TimingModifyInstanceFlag": 1,
        "UpdateTime": "2026-05-29 15:44:11",
        "Vip": "192.168.1.106",
        "VpcId": "vpc-jksnni36",
        "Vport": 3306,
        "Zone": "ap-chengdu-1",
        "Zones": [
            "ap-chengdu-1"
        ],
        "RequestId": "e66bd67d-5e7c-4c57-8630-c926c55b6efb"
    }
}
```

