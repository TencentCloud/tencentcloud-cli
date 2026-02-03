**Example 1: 查看 TDSQL-C 分析集群详情**

查看分析集群的详细信息

Input: 

```
tccli cynosdb DescribeLibraDBClusterDetail --cli-unfold-argument  \
    --ClusterId libradb-i8okw971
```

Output: 
```
{
    "Response": {
        "Detail": {
            "ClusterId": "libradb-i8okw971",
            "ClusterName": "libradb-i8okw971",
            "CreateTime": "2025-05-15 15:42:58",
            "CynosVersion": "",
            "CynosVersionTag": "",
            "DbVersion": "1.2404.21.0",
            "InstanceSet": [
                {
                    "DbMode": "",
                    "InstanceCpu": 4,
                    "InstanceDeviceType": "Common",
                    "InstanceId": "libradb-ins-6231eq34",
                    "InstanceMemory": 16,
                    "InstanceName": "libradb-ins-6231eq34",
                    "InstanceRole": "libradbRo",
                    "InstanceStatus": "running",
                    "InstanceStatusDesc": "运行中",
                    "InstanceStorage": 20,
                    "InstanceStorageType": "CLOUD_TCS",
                    "InstanceType": "libradbRo",
                    "MaintainDuration": 3600,
                    "MaintainStartTime": 10800,
                    "MaintainWeekDays": [
                        "Mon",
                        "Tue",
                        "Wed",
                        "Thu",
                        "Fri",
                        "Sat",
                        "Sun"
                    ],
                    "NodeList": [
                        "libradbn-0"
                    ]
                }
            ],
            "IsFreeze": "no",
            "MasterZone": "ap-guangzhou-7",
            "NoSupportAddRo": "",
            "PayMode": 0,
            "PeriodEndTime": "0001-01-01 00:00:00",
            "PhysicalZone": "",
            "ProjectID": 0,
            "Region": "ap-guangzhou",
            "RenewFlag": 0,
            "RoAddr": [
                {
                    "IP": "172.16.0.67",
                    "Port": 3306
                }
            ],
            "Status": "running",
            "StatusDesc": "运行中",
            "Storage": 20,
            "SubnetId": "subnet-558rhwt2",
            "SubnetName": "Default-Subnet",
            "Tasks": [],
            "UsedStorage": 0,
            "Vip": "172.16.0.67",
            "VpcId": "vpc-nnakli31",
            "VpcName": "Default-VPC",
            "Vport": 3306,
            "Zone": ""
        },
        "RequestId": "7d579362-a249-4dd0-9cf3-d1c68af42d2b"
    }
}
```

