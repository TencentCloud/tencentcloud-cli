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
            "ID": 20230915001,
            "InstanceType": "cdwpg-cn",
            "InstanceName": "analytics-prod-01",
            "Status": "Serving",
            "StatusDesc": "服务中",
            "InstanceStateInfo": {
                "InstanceState": "Serving",
                "FlowCreateTime": "2023-09-15 09:30:00",
                "FlowName": "ClusterScaleOut",
                "FlowProgress": 75,
                "InstanceStateDesc": "集群扩容中",
                "FlowMsg": "正在添加3个计算节点",
                "ProcessName": "资源扩容中",
                "BackupStatus": 0,
                "RequestId": "req-5f82b735",
                "BackupOpenStatus": 1
            },
            "InstanceID": "inst-9d7e2f4a",
            "CreateTime": "2023-01-15 14:20:00",
            "Region": "ap-shanghai",
            "Zone": "ap-shanghai-2",
            "RegionDesc": "上海地域",
            "ZoneDesc": "上海二区",
            "Tags": [
                {
                    "TagKey": "Environment",
                    "TagValue": "Production"
                },
                {
                    "TagKey": "Department",
                    "TagValue": "DataAnalytics"
                }
            ],
            "Version": "v3.2.1",
            "Charset": "UTF-8",
            "CNNodes": [
                {
                    "SpecName": "CN8x32",
                    "DataDisk": {
                        "DiskCount": 2,
                        "MaxDiskSize": 2048,
                        "MinDiskSize": 512,
                        "DiskType": "Cloud_SSD",
                        "DiskDesc": "高性能云盘",
                        "CvmClass": "S5.MEDIUM8"
                    },
                    "CvmCount": 3
                }
            ],
            "DNNodes": [
                {
                    "SpecName": "DN4x64",
                    "DataDisk": {
                        "DiskCount": 4,
                        "MaxDiskSize": 4096,
                        "MinDiskSize": 1024,
                        "DiskType": "Cloud_Premium",
                        "DiskDesc": "企业级云盘",
                        "CvmClass": "S5.LARGE16"
                    },
                    "CvmCount": 2
                }
            ],
            "RegionId": 21,
            "ZoneId": 210002,
            "VpcId": "vpc-89f2d1e3",
            "SubnetId": "subnet-45c9b2f1",
            "ExpireTime": "2025-12-31 23:59:59",
            "PayMode": "PrePaid",
            "RenewFlag": true,
            "InstanceId": "cluster-9a8b7c6d",
            "AccessDetails": [
                {
                    "Address": "10.16.32.45:3306",
                    "Protocol": "MySQL"
                }
            ]
        },
        "RequestId": "xdsx"
    }
}
```

