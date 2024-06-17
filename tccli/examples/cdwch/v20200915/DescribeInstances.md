**Example 1: 获取实例列表**

获取某个用户下所有的集群列表信息

Input: 

```
tccli cdwch DescribeInstances --cli-unfold-argument  \
    --Limit 10 \
    --SearchInstanceName  \
    --SearchInstanceId  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9b38c8fb-ea36-4330-asdf-xxxxxxx",
        "TotalCount": 1,
        "InstancesList": [
            {
                "Id": 3103,
                "InstanceId": "cdwch-xxxxx",
                "InstanceName": "axvc",
                "Status": "Serving",
                "StatusDesc": "运行中",
                "InstanceStateInfo": {
                    "InstanceState": "",
                    "InstanceStateDesc": "",
                    "FlowCreateTime": "",
                    "FlowName": "",
                    "FlowProgress": 0,
                    "FlowMsg": "",
                    "ProcessName": "",
                    "ProcessSubName": "",
                    "RequestId": ""
                },
                "Version": "23.8.9.1",
                "Region": "ap-bangkok",
                "RegionDesc": "曼谷",
                "RegionId": 23,
                "Zone": "ap-bangkok-2",
                "ZoneDesc": "曼谷二区",
                "VpcId": "vpc-456nv6lg",
                "SubnetId": "subnet-b0ubaq61",
                "PayMode": "PREPAID",
                "CreateTime": "2024-05-23 14:38:46",
                "ExpireTime": "2024-06-23 14:38:46",
                "MasterSummary": {
                    "Spec": "SCH6",
                    "SubProductType": "STANDARD",
                    "SpecCore": 4,
                    "SpecMemory": 16,
                    "NodeSize": 1,
                    "Core": 4,
                    "Memory": 16,
                    "Disk": 200,
                    "DiskCount": 10,
                    "MaxDiskSize": 320000,
                    "DiskType": "CLOUD_HSSD",
                    "DiskDesc": "增强型SSD云硬盘",
                    "Encrypt": 0,
                    "AttachCBSSpec": {
                        "DiskType": "",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskDesc": ""
                    }
                },
                "CommonSummary": null,
                "HA": "false",
                "AccessInfo": "[{\"address\":\"10.0.0.7:9000\",\"protocol\":\"tcp\"},{\"address\":\"10.0.0.7:8123\",\"protocol\":\"http\"},{\"address\":\"10.0.0.7:9004\",\"protocol\":\"mysql_tcp\"}]",
                "FlowMsg": "",
                "RenewFlag": false,
                "Tags": null,
                "Monitor": "",
                "HasClsTopic": false,
                "ClsTopicId": "",
                "ClsLogSetId": "",
                "HasEsIndex": false,
                "EsIndexId": "",
                "EsIndexUsername": "",
                "EsIndexPassword": "",
                "CosBucketName": "",
                "Eip": "",
                "EnableXMLConfig": 0,
                "CosMoveFactor": 0,
                "CanAttachCbs": false,
                "CanAttachCbsLvm": false,
                "CanAttachCos": true,
                "Components": null,
                "Kind": "external",
                "UpgradeVersions": null,
                "IsElastic": false,
                "HAZk": false,
                "CHProxyVip": "",
                "MountDiskType": 0,
                "IsSecondaryZone": false,
                "SecondaryZoneInfo": ""
            }
        ]
    }
}
```

