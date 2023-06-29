**Example 1: 描述实例信息**

根据实例ID查询某个实例的具体信息

Input: 

```
tccli cdwch DescribeInstance --cli-unfold-argument  \
    --InstanceId cdwch-12345678
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
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
                "MaxDiskSize": 0,
                "Encrypt": 0
            },
            "CommonSummary": {
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
                "MaxDiskSize": 0,
                "Encrypt": 0
            },
            "HA": "abc",
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
            "IsElastic": true,
            "InstanceStateInfo": {
                "InstanceState": "abc",
                "FlowCreateTime": "abc",
                "FlowName": "abc",
                "FlowProgress": 0,
                "InstanceStateDesc": "abc",
                "FlowMsg": "abc",
                "ProcessName": "abc",
                "RequestId": "abc"
            },
            "HAZk": true,
            "MountDiskType": 0,
            "CHProxyVip": "abc",
            "CosBucketName": "abc",
            "CanAttachCbs": true,
            "CanAttachCbsLvm": true,
            "CanAttachCos": true,
            "Components": [
                {
                    "Name": "abc",
                    "Version": "abc"
                }
            ],
            "UpgradeVersions": "abc"
        },
        "RequestId": "abc"
    }
}
```

