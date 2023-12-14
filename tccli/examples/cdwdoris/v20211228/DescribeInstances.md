**Example 1: 获取实例列表**

获取某个用户下所有的集群列表信息

Input: 

```
tccli cdwdoris DescribeInstances --cli-unfold-argument  \
    --Limit 10 \
    --SearchInstanceName  \
    --SearchInstanceId  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Status": "abc",
                "Version": "abc",
                "Region": "abc",
                "Zone": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "PayMode": "abc",
                "CreateTime": "abc",
                "ExpireTime": "abc",
                "MasterSummary": {
                    "Spec": "abc",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "abc",
                    "DiskDesc": "abc",
                    "AttachCBSSpec": {
                        "DiskType": "abc",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "abc"
                    },
                    "SubProductType": "abc",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "Encrypt": 0,
                    "MaxDiskSize": 0
                },
                "CoreSummary": {
                    "Spec": "abc",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "abc",
                    "DiskDesc": "abc",
                    "AttachCBSSpec": {
                        "DiskType": "abc",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "abc"
                    },
                    "SubProductType": "abc",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "Encrypt": 0,
                    "MaxDiskSize": 0
                },
                "HA": "abc",
                "HaType": 0,
                "AccessInfo": "abc",
                "Id": 0,
                "RegionId": 0,
                "ZoneDesc": "abc",
                "FlowMsg": "abc",
                "StatusDesc": "abc",
                "RenewFlag": true,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "Monitor": "abc",
                "HasClsTopic": true,
                "ClsTopicId": "abc",
                "ClsLogSetId": "abc",
                "EnableXMLConfig": 0,
                "RegionDesc": "abc",
                "Eip": "abc",
                "CosMoveFactor": 0,
                "Kind": "abc",
                "CosBucketName": "abc",
                "CanAttachCbs": true,
                "BuildVersion": "abc",
                "Components": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

