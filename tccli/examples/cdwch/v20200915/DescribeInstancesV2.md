**Example 1: 获取实例列表v2**

供cvm侧调用

Input: 

```
tccli cdwch DescribeInstancesV2 --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --Zone abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
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
                        "RequestId": "abc",
                        "ProcessSubName": "abc"
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
                    "UpgradeVersions": "abc",
                    "EsIndexId": "abc",
                    "EsIndexUsername": "abc",
                    "EsIndexPassword": "abc",
                    "HasEsIndex": true,
                    "IsSecondaryZone": true,
                    "SecondaryZoneInfo": "abc",
                    "ClickHouseKeeper": true,
                    "Details": {
                        "EnableAlarmStrategy": true
                    },
                    "IsWhiteSGs": true,
                    "BindSGs": [
                        "abc"
                    ]
                },
                "Uin": "abc",
                "AppId": 0,
                "TotalCvms": [
                    {
                        "Id": 1,
                        "Appid": 0,
                        "Region": "abc",
                        "CvmInstanceId": "abc",
                        "InstanceType": "abc",
                        "Ip": "abc",
                        "Cpu": 0,
                        "Memory": 0,
                        "InstanceName": "abc",
                        "ChargeType": "abc",
                        "RenewFlag": "abc",
                        "CreateTime": "abc",
                        "ExpireTime": "abc",
                        "OsName": "abc",
                        "InstanceState": "abc",
                        "Uuid": "abc",
                        "VpcId": "abc",
                        "SubnetId": "abc",
                        "CdwInstanceId": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

