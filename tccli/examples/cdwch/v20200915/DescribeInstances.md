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
        "InstancesList": [
            {
                "AccessInfo": "[{\"address\":\"10.0.12.47:9000\",\"protocol\":\"tcp\",\"address_public\":\"\"},{\"address\":\"10.0.12.47:8123\",\"protocol\":\"http\",\"address_public\":\"\"},{\"address\":\"10.0.12.47:9004\",\"protocol\":\"mysql_tcp\",\"address_public\":\"\"}]",
                "BindSGs": [],
                "CHProxyVip": "",
                "CanAttachCbs": false,
                "CanAttachCbsLvm": false,
                "CanAttachCos": true,
                "ClickHouseKeeper": false,
                "ClsLogSetId": "",
                "ClsTopicId": "",
                "CommonSummary": {
                    "AttachCBSSpec": {
                        "DiskCount": 0,
                        "DiskDesc": "",
                        "DiskSize": 0,
                        "DiskType": ""
                    },
                    "Core": 2,
                    "Disk": 100,
                    "DiskCount": 1,
                    "DiskDesc": "增强型SSD云硬盘",
                    "DiskType": "CLOUD_HSSD",
                    "Encrypt": 0,
                    "MaxDiskSize": 32000,
                    "Memory": 4,
                    "NodeSize": 3,
                    "Spec": "S_2_4_H",
                    "SpecCore": 2,
                    "SpecMemory": 4,
                    "SubProductType": "STANDARD"
                },
                "Components": [],
                "CosBucketName": "",
                "CosMoveFactor": 0,
                "CreateTime": "2025-04-23 11:12:37",
                "Details": {
                    "EnableAlarmStrategy": true
                },
                "Eip": "",
                "EnableXMLConfig": 0,
                "EsIndexId": "",
                "EsIndexPassword": "",
                "EsIndexUsername": "",
                "ExpireTime": "0000.00.00 00:00:00",
                "FlowMsg": "",
                "HA": "true",
                "HAZk": true,
                "HasClsTopic": true,
                "HasEsIndex": false,
                "HasPublicCloudClb": false,
                "Id": 2228,
                "InstanceId": "cdwch-qualfsfr",
                "InstanceName": "测试备份恢复功能可删除",
                "InstanceStateInfo": {
                    "FlowCreateTime": "",
                    "FlowMsg": "",
                    "FlowName": "",
                    "FlowProgress": 0,
                    "InstanceState": "",
                    "InstanceStateDesc": "",
                    "ProcessName": "",
                    "ProcessSubName": "",
                    "RequestId": ""
                },
                "IsElastic": false,
                "IsSecondaryZone": false,
                "IsWhiteSGs": false,
                "Kind": "external",
                "MasterSummary": {
                    "AttachCBSSpec": {
                        "DiskCount": 0,
                        "DiskDesc": "",
                        "DiskSize": 0,
                        "DiskType": ""
                    },
                    "Core": 2,
                    "Disk": 200,
                    "DiskCount": 10,
                    "DiskDesc": "增强型SSD云硬盘",
                    "DiskType": "CLOUD_HSSD",
                    "Encrypt": 0,
                    "MaxDiskSize": 320000,
                    "Memory": 4,
                    "NodeSize": 4,
                    "Spec": "S_2_4_H",
                    "SpecCore": 2,
                    "SpecMemory": 4,
                    "SubProductType": "STANDARD"
                },
                "Monitor": "",
                "MountDiskType": 0,
                "PayMode": "POSTPAID_BY_HOUR",
                "Region": "ap-chongqing",
                "RegionDesc": "重庆",
                "RegionId": 19,
                "RenewFlag": false,
                "SecondaryZoneInfo": "",
                "Status": "Serving",
                "StatusDesc": "运行中",
                "SubnetId": "subnet-hihquo9a",
                "Tags": [],
                "UpgradeVersions": "",
                "Version": "23.8.9.1",
                "VpcId": "vpc-9dsabpv9",
                "Zone": "ap-chongqing-1",
                "ZoneDesc": "重庆一区"
            }
        ],
        "RequestId": "4c8fd172-c7ef-4900-a073-ed35687c12ea",
        "TotalCount": 1
    }
}
```

