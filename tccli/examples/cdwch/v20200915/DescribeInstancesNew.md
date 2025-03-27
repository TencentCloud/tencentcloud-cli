**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli cdwch DescribeInstancesNew --cli-unfold-argument  \
    --SearchInstanceId cdwch-xxx \
    --SearchInstanceName testname \
    --Offset 0 \
    --Limit 0 \
    --SearchTags.0.TagKey testname \
    --SearchTags.0.TagValue testname \
    --SearchTags.0.AllValue 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "InstanceId": "testname",
                "InstanceName": "testname",
                "Status": "testname",
                "Version": "testname",
                "Region": "testname",
                "Zone": "testname",
                "VpcId": "testname",
                "SubnetId": "testname",
                "PayMode": "testname",
                "CreateTime": "testname",
                "ExpireTime": "testname",
                "MasterSummary": {
                    "Spec": "testname",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "testname",
                    "DiskDesc": "testname",
                    "AttachCBSSpec": {
                        "DiskType": "testname",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "testname"
                    },
                    "SubProductType": "testname",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "MaxDiskSize": 0,
                    "Encrypt": 0
                },
                "CommonSummary": {
                    "Spec": "testname",
                    "NodeSize": 0,
                    "Core": 0,
                    "Memory": 0,
                    "Disk": 0,
                    "DiskType": "testname",
                    "DiskDesc": "testname",
                    "AttachCBSSpec": {
                        "DiskType": "testname",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": "testname"
                    },
                    "SubProductType": "testname",
                    "SpecCore": 0,
                    "SpecMemory": 0,
                    "DiskCount": 0,
                    "MaxDiskSize": 0,
                    "Encrypt": 0
                },
                "HA": "testname",
                "AccessInfo": "testname",
                "Id": 0,
                "RegionId": 0,
                "ZoneDesc": "testname",
                "FlowMsg": "testname",
                "StatusDesc": "testname",
                "RenewFlag": true,
                "Tags": [
                    {
                        "TagKey": "testname",
                        "TagValue": "testname"
                    }
                ],
                "Monitor": "testname",
                "HasClsTopic": true,
                "ClsTopicId": "testname",
                "ClsLogSetId": "testname",
                "EnableXMLConfig": 0,
                "RegionDesc": "testname",
                "Eip": "testname",
                "CosMoveFactor": 0,
                "Kind": "testname",
                "IsElastic": true,
                "InstanceStateInfo": {
                    "InstanceState": "testname",
                    "FlowCreateTime": "testname",
                    "FlowName": "testname",
                    "FlowProgress": 0,
                    "InstanceStateDesc": "testname",
                    "FlowMsg": "testname",
                    "ProcessName": "testname",
                    "RequestId": "testname"
                },
                "HAZk": true,
                "MountDiskType": 0,
                "CHProxyVip": "testname",
                "CosBucketName": "testname",
                "CanAttachCbs": true,
                "CanAttachCbsLvm": true,
                "CanAttachCos": true,
                "Components": [
                    {
                        "Name": "testname",
                        "Version": "testname"
                    }
                ],
                "UpgradeVersions": "testname"
            }
        ],
        "RequestId": "testname"
    }
}
```

