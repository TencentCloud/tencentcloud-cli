**Example 1: 描述实例信息**

根据实例ID查询某个实例的具体信息

Input: 

```
tccli cdwpg DescribeInstance --cli-unfold-argument  \
    --InstanceId cdwpg-xdx
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
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
            "InstanceType": "TbaseV3",
            "PayMode": "POSTPAID_BY_HOUR",
            "Region": "ap-chongqing",
            "RenewFlag": false,
            "SubnetId": "subnet-rdlodajk",
            "Tags": [],
            "Version": "3.16.9.4",
            "VpcId": "vpc-1asw4o73",
            "Zone": "ap-chongqing-1"
        },
        "RequestId": "d7cde91a-be80-4297-ac48-a5eebd63a397"
    }
}
```

