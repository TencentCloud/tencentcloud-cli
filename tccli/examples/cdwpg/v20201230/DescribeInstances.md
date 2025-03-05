**Example 1: 查询云原生实例列表**



Input: 

```
tccli cdwpg DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --SearchTags.0.AllValue 0 \
    --SearchTags.0.TagKey test \
    --SearchTags.0.TagValue test \
    --SearchInstanceId test \
    --SearchInstanceName test
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxxx-xxxxx-xxxxx",
        "TotalCount": 2,
        "ErrorMsg": "",
        "InstancesList": [
            {
                "ID": 12345,
                "InstanceType": "cdwpg-cn",
                "InstanceName": "cdwpg-example",
                "Status": "Running",
                "StatusDesc": "运行中",
                "InstanceStateInfo": {
                    "InstanceState": "Serving",
                    "FlowCreateTime": "2023-04-10T15:30:00Z",
                    "FlowName": "CreateCluster",
                    "FlowProgress": 50,
                    "InstanceStateDesc": "运行中",
                    "FlowMsg": "",
                    "ProcessName": "购买资源中",
                    "BackupStatus": 0,
                    "RequestId": "req-1234567890",
                    "BackupOpenStatus": 1
                },
                "InstanceID": "cdwpg-ddd",
                "CreateTime": "2022-09-05 20:00:01",
                "Region": "ap-chongqing",
                "Zone": "ap-chongqing-1",
                "RegionDesc": "重庆区域",
                "ZoneDesc": "重庆可用区1",
                "Tags": [
                    {
                        "TagKey": "Environment",
                        "TagValue": "Production"
                    }
                ],
                "Version": "v3",
                "Charset": "UTF-8",
                "CNNodes": [
                    {
                        "SpecName": "high-cpu",
                        "DataDisk": {
                            "DiskCount": 2,
                            "MaxDiskSize": 1024,
                            "MinDiskSize": 256,
                            "DiskType": "SSD",
                            "DiskDesc": "高性能固态硬盘",
                            "CvmClass": "标准型S3"
                        },
                        "CvmCount": 2
                    }
                ],
                "DNNodes": [
                    {
                        "SpecName": "high-cpu",
                        "DataDisk": {
                            "DiskCount": 2,
                            "MaxDiskSize": 1024,
                            "MinDiskSize": 256,
                            "DiskType": "SSD",
                            "DiskDesc": "高性能固态硬盘",
                            "CvmClass": "标准型S3"
                        },
                        "CvmCount": 2
                    }
                ],
                "RegionId": 1,
                "ZoneId": 101,
                "VpcId": "vpc-12345678",
                "SubnetId": "subnet-87654321",
                "ExpireTime": "2023-09-05 20:00:01",
                "PayMode": "Postpaid",
                "RenewFlag": true,
                "InstanceId": "instance-abcdefg",
                "AccessDetails": [
                    {
                        "Address": "10.0.123.x",
                        "Protocol": "ddd"
                    }
                ]
            }
        ]
    }
}
```

