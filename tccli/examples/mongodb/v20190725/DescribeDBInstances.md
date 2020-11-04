**Example 1: 查询实例列表**



Input: 

```
tccli mongodb DescribeDBInstances --cli-unfold-argument  \
    --Limit 1
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
                "CpuNum": 2,
                "CreateTime": "2019-04-02 19:29:16",
                "DeadLine": "2019-04-04 19:29:16",
                "InstanceId": "cmgo-rw2v134z",
                "InstanceName": "cmgo-rw2v134z",
                "InstanceStatusDesc": "回档中",
                "InstanceType": 2,
                "InstanceVer": 4,
                "MachineType": "HIO10G",
                "MaintenanceEnd": "05:00:00",
                "MaintenanceStart": "04:00:00",
                "Memory": 4096,
                "MongoVersion": "MONGO_3_WT",
                "NetType": 1,
                "PayMode": 0,
                "ProjectId": 0,
                "Protocol": 0,
                "ReadonlyInstances": [],
                "RealInstanceId": "cmgo-da0pc0dr",
                "Region": "ap-guangzhou",
                "RelatedInstance": {
                    "InstanceId": "",
                    "Region": ""
                },
                "ReplicaSets": [
                    {
                        "Memory": 4096,
                        "OplogSize": 10240,
                        "RealReplicaSetId": "cmgo-rw2v134z_0",
                        "ReplicaSetId": "cmgo-rw2v134z_0",
                        "ReplicaSetName": "cmgo-rw2v134z_0",
                        "SecondaryNum": 2,
                        "UsedVolume": 0,
                        "Volume": 102400
                    }
                ],
                "ReplicationSetNum": 1,
                "SecondaryNum": 2,
                "StandbyInstances": [],
                "Status": 1,
                "SubnetId": "subnet-b0lagkxi",
                "Tags": [],
                "UsedVolume": 0,
                "Vip": "",
                "Volume": 102400,
                "VpcId": "vpc-orgohlut",
                "Vport": 27017,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "302530d2-ee57-495e-89d0-51e03b11815e",
        "TotalCount": 19
    }
}
```

