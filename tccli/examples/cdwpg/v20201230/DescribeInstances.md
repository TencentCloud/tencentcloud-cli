**Example 1: 查询云原生实例列表**



Input: 

```
tccli cdwpg DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "InstancesList": [
            {
                "AccessDetails": [
                    {
                        "Address": "10.0.16.19:9000",
                        "Protocol": "tcp"
                    }
                ],
                "CNNodes": [
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H_CN"
                    }
                ],
                "Charset": "UTF8",
                "CreateTime": "2025-03-19 16:37:38",
                "DNNodes": [
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "增强型SSD云硬盘",
                            "DiskType": "CLOUD_HSSD",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_H"
                    }
                ],
                "ExpireTime": "0000.00.00 00:00:00",
                "ID": 1094,
                "InstanceId": "cdwpg-rzshdeh1",
                "InstanceName": "hugogao_test",
                "InstanceStateInfo": {
                    "BackupOpenStatus": 0,
                    "BackupStatus": 0,
                    "FlowCreateTime": "",
                    "FlowMsg": "",
                    "FlowName": "",
                    "FlowProgress": 0,
                    "InstanceState": "Serving",
                    "InstanceStateDesc": "运行中",
                    "ProcessName": "",
                    "RequestId": ""
                },
                "InstanceType": "TbaseV3",
                "PayMode": "POSTPAID_BY_HOUR",
                "Region": "ap-chongqing",
                "RegionDesc": "重庆",
                "RegionId": 19,
                "RenewFlag": false,
                "Status": "Serving",
                "StatusDesc": "运行中",
                "SubnetId": "subnet-rdlodajk",
                "Tags": [],
                "Version": "3.16.9.4",
                "VpcId": "vpc-1asw4o73",
                "Zone": "ap-chongqing-1",
                "ZoneDesc": "重庆一区",
                "ZoneId": 190001
            },
            {
                "AccessDetails": [
                    {
                        "Address": "10.0.16.27:9000",
                        "Protocol": "tcp"
                    }
                ],
                "CNNodes": [
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P_CN"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 1,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 32000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P_CN"
                    }
                ],
                "Charset": "UTF8",
                "CreateTime": "2025-02-20 11:37:11",
                "DNNodes": [
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P"
                    },
                    {
                        "CvmCount": 2,
                        "DataDisk": {
                            "CvmClass": "STANDARD",
                            "DiskCount": 10,
                            "DiskDesc": "高性能云硬盘",
                            "DiskType": "CLOUD_PREMIUM",
                            "MaxDiskSize": 320000,
                            "MinDiskSize": 200
                        },
                        "SpecName": "S_4_16_P"
                    }
                ],
                "ExpireTime": "0000.00.00 00:00:00",
                "ID": 1089,
                "InstanceId": "cdwpg-9jcyk7yp",
                "InstanceName": "demo_tim",
                "InstanceStateInfo": {
                    "BackupOpenStatus": 1,
                    "BackupStatus": 0,
                    "FlowCreateTime": "",
                    "FlowMsg": "",
                    "FlowName": "",
                    "FlowProgress": 0,
                    "InstanceState": "Serving",
                    "InstanceStateDesc": "运行中",
                    "ProcessName": "",
                    "RequestId": ""
                },
                "InstanceType": "TbaseV3",
                "PayMode": "POSTPAID_BY_HOUR",
                "Region": "ap-chongqing",
                "RegionDesc": "重庆",
                "RegionId": 19,
                "RenewFlag": false,
                "Status": "Serving",
                "StatusDesc": "运行中",
                "SubnetId": "subnet-rdlodajk",
                "Tags": [],
                "Version": "3.16.9.4",
                "VpcId": "vpc-1asw4o73",
                "Zone": "ap-chongqing-1",
                "ZoneDesc": "重庆一区",
                "ZoneId": 190001
            }
        ],
        "RequestId": "4ce96c66-e75b-4ec2-aa3c-06594ea15916",
        "TotalCount": 2
    }
}
```

