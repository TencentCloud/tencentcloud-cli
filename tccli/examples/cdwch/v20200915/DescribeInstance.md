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
            "InstanceId": "cdwch-xxxxxxxx",
            "InstanceName": "测试集群",
            "Status": "Serving",
            "Version": "23.8.9.1",
            "Region": "ap-guangzhou",
            "Zone": "ap-guangzhou-1",
            "VpcId": "vpc-xxxxxxxx",
            "SubnetId": "subnet-xxxxxxxx",
            "PayMode": "PREPAID",
            "CreateTime": "2025-02-28 11:34:45",
            "ExpireTime": "2025-03-28 11:34:46",
            "MasterSummary": {
                "Spec": "H_32_128",
                "NodeSize": 1,
                "Core": 32,
                "Memory": 128,
                "Disk": 7140,
                "DiskType": "LOCAL_BASIC",
                "DiskDesc": "本地盘",
                "AttachCBSSpec": {
                    "DiskType": "",
                    "DiskSize": 0,
                    "DiskCount": 0,
                    "DiskDesc": ""
                },
                "SubProductType": "HIGHIO",
                "SpecCore": 32,
                "SpecMemory": 128,
                "DiskCount": 2,
                "MaxDiskSize": 7140,
                "Encrypt": 0
            },
            "CommonSummary": {
                "Spec": "S_2_4_P",
                "NodeSize": 3,
                "Core": 2,
                "Memory": 4,
                "Disk": 100,
                "DiskType": "CLOUD_PREMIUM",
                "DiskDesc": "高性能云盘",
                "AttachCBSSpec": {
                    "DiskType": "",
                    "DiskSize": 0,
                    "DiskCount": 0,
                    "DiskDesc": ""
                },
                "SubProductType": "STANDARD",
                "SpecCore": 2,
                "SpecMemory": 4,
                "DiskCount": 1,
                "MaxDiskSize": 32000,
                "Encrypt": 0
            },
            "HA": "false",
            "AccessInfo": "[{\"address\":\"10.x.x.xx:9000\",\"protocol\":\"tcp\",\"address_public\":\"\"},{\"address\":\"10.x.x.xx:8123\",\"protocol\":\"http\",\"address_public\":\"\"},{\"address\":\"10.x.x.xx:9004\",\"protocol\":\"mysql_tcp\",\"address_public\":\"\"}]",
            "Id": 3857,
            "RegionId": 1,
            "ZoneDesc": "广州一区",
            "FlowMsg": "",
            "StatusDesc": "运行中",
            "RenewFlag": true,
            "Tags": [
                {
                    "TagKey": "产品名称",
                    "TagValue": "cdwch"
                }
            ],
            "Monitor": "",
            "HasClsTopic": false,
            "ClsTopicId": "",
            "ClsLogSetId": "",
            "EnableXMLConfig": 0,
            "RegionDesc": "广州",
            "Eip": "",
            "CosMoveFactor": 0,
            "Kind": "external",
            "IsElastic": true,
            "InstanceStateInfo": {
                "InstanceState": "",
                "FlowCreateTime": "",
                "FlowName": "",
                "FlowProgress": 0,
                "InstanceStateDesc": "",
                "FlowMsg": "",
                "ProcessName": "",
                "RequestId": ""
            },
            "HAZk": true,
            "MountDiskType": 0,
            "CHProxyVip": "",
            "CosBucketName": "",
            "CanAttachCbs": true,
            "CanAttachCbsLvm": true,
            "CanAttachCos": true,
            "Components": [],
            "UpgradeVersions": ""
        },
        "RequestId": "asdfaes-xad12x-123axafg"
    }
}
```

