**Example 1: 查询实例列表**

获取当前uin已授权的实例列表

Input: 

```
tccli mongodb DescribeDBInstances --cli-unfold-argument  \
    --Status 0 \
    --OrderBy xx \
    --InstanceIds xx \
    --VpcId xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --ClusterType 0 \
    --PayMode 0 \
    --Limit 1 \
    --SearchKey xx \
    --Offset 1 \
    --SubnetId xx \
    --OrderByType xx \
    --InstanceType 0 \
    --ProjectIds 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "InstanceDetails": [
            {
                "ConfigServerMemory": 1,
                "Zone": "xx",
                "MongosNodeNum": 1,
                "ReadonlyInstances": [
                    {
                        "InstanceId": "xx",
                        "Region": "xx"
                    }
                ],
                "RelatedInstance": "xx",
                "AutoRenewFlag": 0,
                "DeadLine": "2020-09-22 00:00:00",
                "Memory": 1,
                "StandbyInstances": [
                    {
                        "InstanceId": "xx",
                        "Region": "xx"
                    }
                ],
                "InstanceVer": 1,
                "MaintenanceStart": "xx",
                "RealInstanceId": "xx",
                "CpuNum": 1,
                "MaintenanceEnd": "xx",
                "VpcId": "xx",
                "CloneInstances": [
                    {
                        "InstanceId": "xx",
                        "Region": "xx"
                    }
                ],
                "InstanceId": "xx",
                "ConfigServerCpuNum": 1,
                "Volume": 1,
                "SecondaryNum": 1,
                "NetType": 1,
                "MongoVersion": "xx",
                "ReplicationSetNum": 1,
                "ReplicaSets": [
                    {
                        "UsedVolume": 0.0,
                        "ReplicaSetId": "xx",
                        "Volume": 1,
                        "SecondaryNum": 1,
                        "OplogSize": 1,
                        "Memory": 1,
                        "ReplicaSetName": "xx",
                        "RealReplicaSetId": "xx"
                    }
                ],
                "InstanceType": 1,
                "Status": 1,
                "ProjectId": 1,
                "ClusterType": 1,
                "PayMode": 1,
                "SubnetId": "xx",
                "ClusterVer": 1,
                "MongosCpuNum": 1,
                "ReadonlyNodeNum": 1,
                "Protocol": 1,
                "InstanceName": "xx",
                "MongosMemory": 1,
                "MachineType": "xx",
                "InstanceStatusDesc": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "UsedVolume": 1,
                "Vip": "xx",
                "ConfigServerVolume": 1,
                "Region": "xx",
                "ConfigServerNodeNum": 1,
                "Vport": 1,
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

