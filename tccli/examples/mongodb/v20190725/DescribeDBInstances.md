**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli mongodb DescribeDBInstances --cli-unfold-argument  \
    --Status 0 \
    --OrderBy DESC \
    --InstanceIds cmgo-3vgr**** \
    --VpcId vpc-gfb3**** \
    --Tags.0.TagKey test \
    --Tags.0.TagValue testValue \
    --ClusterType 0 \
    --PayMode 0 \
    --Limit 1 \
    --SearchKey  \
    --Offset 1 \
    --SubnetId  \
    --OrderByType  \
    --InstanceType 0 \
    --ProjectIds 1
```

Output: 
```
{
    "Response": {
        "InstanceDetails": [
            {
                "AutoRenewFlag": 0,
                "CloneInstances": [],
                "ClusterType": 0,
                "ClusterVer": 1,
                "ConfigServerCpuNum": 0,
                "ConfigServerMemory": 0,
                "ConfigServerNodeNum": 3,
                "ConfigServerVolume": 0,
                "CpuNum": 2,
                "CreateTime": "2023-03-30 07:44:21",
                "DeadLine": "2073-03-30 07:44:21",
                "InstanceId": "cmgo-3vgr****",
                "InstanceName": "测试实例",
                "InstanceStatusDesc": "运行中",
                "InstanceType": 1,
                "InstanceVer": 4,
                "MachineType": "HIO10G",
                "MaintenanceEnd": "05:00:00",
                "MaintenanceStart": "04:00:00",
                "Memory": 4096,
                "MongoVersion": "MONGO_42_WT",
                "MongosCpuNum": 0,
                "MongosMemory": 0,
                "MongosNodeNum": 0,
                "NetType": 1,
                "PayMode": 0,
                "ProjectId": 0,
                "Protocol": 0,
                "ReadonlyInstances": [],
                "ReadonlyNodeNum": 0,
                "RealInstanceId": "cmgo-3vgr****",
                "Region": "ap-guangzhou",
                "RelatedInstance": {
                    "InstanceId": "",
                    "Region": ""
                },
                "ReplicaSets": [
                    {
                        "Memory": 4096,
                        "OplogSize": 1024,
                        "RealReplicaSetId": "cmgo-3vgrapm5_*",
                        "ReplicaSetId": "cmgo-3vgrapm5_*",
                        "ReplicaSetName": "cmgo-3vgrapm5_*",
                        "SecondaryNum": 2,
                        "UsedVolume": 315,
                        "Volume": 10240
                    }
                ],
                "ReplicationSetNum": 1,
                "SecondaryNum": 2,
                "StandbyInstances": [],
                "Status": 2,
                "SubnetId": "subnet-7q7d****",
                "Tags": [],
                "UsedVolume": 315,
                "Vip": "10.5.2.12;10.5.2.14;10.5.2.10",
                "Volume": 10240,
                "VpcId": "vpc-gfb3****",
                "Vport": 27017,
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "230c9c0e-a56f-4639-81ee-3cb46905c087",
        "TotalCount": 1
    }
}
```

