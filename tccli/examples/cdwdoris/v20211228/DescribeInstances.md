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
                "InstanceId": "str",
                "InstanceName": "str",
                "Status": "str",
                "Version": "str",
                "Region": "str",
                "Zone": "str",
                "VpcId": "str",
                "SubnetId": "str",
                "PayMode": "str",
                "CreateTime": "str",
                "ExpireTime": "str",
                "MasterSummary": {
                    "Spec": "str",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "str",
                    "DiskDesc": "str",
                    "AttachCBSSpec": {
                        "DiskType": "str",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "str"
                    },
                    "SubProductType": "str",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "Encrypt": 0,
                    "MaxDiskSize": 0
                },
                "CoreSummary": {
                    "Spec": "str",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "str",
                    "DiskDesc": "str",
                    "AttachCBSSpec": {
                        "DiskType": "str",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "str"
                    },
                    "SubProductType": "str",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "Encrypt": 0,
                    "MaxDiskSize": 0
                },
                "HA": "str",
                "HaType": 0,
                "AccessInfo": "str",
                "Id": 0,
                "RegionId": 0,
                "ZoneDesc": "str",
                "FlowMsg": "str",
                "StatusDesc": "str",
                "RenewFlag": true,
                "Tags": [
                    {
                        "TagKey": "str",
                        "TagValue": "str"
                    }
                ],
                "Monitor": "str",
                "HasClsTopic": true,
                "ClsTopicId": "str",
                "ClsLogSetId": "str",
                "EnableXMLConfig": 0,
                "RegionDesc": "str",
                "Eip": "str",
                "CosMoveFactor": 0,
                "Kind": "str",
                "CosBucketName": "str",
                "CanAttachCbs": true,
                "BuildVersion": "str",
                "Components": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

