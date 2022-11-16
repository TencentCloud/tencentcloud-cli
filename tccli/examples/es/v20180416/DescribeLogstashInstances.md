**Example 1: 查询Logstash实例**

根据给定条件查询符合条件的Logstash实例并返回详细信息

Input: 

```
tccli es DescribeLogstashInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceList": [
            {
                "InstanceId": "ls-ee6o1285",
                "InstanceName": "wurong-20200927-ls01",
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "AppId": 1257780094,
                "Uin": "100007799884",
                "VpcId": "vpc-ck9abamb",
                "SubnetId": "subnet-gmmt588q",
                "Status": 1,
                "ChargeType": "POSTPAID_BY_HOUR",
                "ChargePeriod": 0,
                "RenewFlag": "",
                "NodeType": "LOGSTASH.S1.MEDIUM4",
                "NodeNum": 5,
                "DiskType": "CLOUD_SSD",
                "DiskSize": 100,
                "LogstashVersion": "6.8.10",
                "LicenseType": "xpack",
                "YMLConfig": "",
                "BindedESInstanceId": "",
                "Nodes": [
                    {
                        "NodeId": "100003160102096307",
                        "Ip": "10.0.3.21",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160102096308",
                        "Ip": "10.0.3.134",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160102514909",
                        "Ip": "10.0.3.151",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160102514910",
                        "Ip": "10.0.3.160",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160102514911",
                        "Ip": "10.0.3.157",
                        "Port": 9600
                    }
                ],
                "ExtendedFiles": [
                    {
                        "Name": "xx",
                        "Size": 1
                    }
                ],
                "CpuNum": 1,
                "MemSize": 1,
                "OperationDuration": {
                    "TimeStart": "xx",
                    "TimeZone": "xx",
                    "Periods": [
                        1
                    ],
                    "TimeEnd": "xx"
                },
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CreateTime": "2020-09-25 16:02:43",
                "UpdateTime": "2020-09-27 16:10:17",
                "Deadline": "2017-12-04 00:00:00"
            },
            {
                "InstanceId": "ls-g8k9pzj9",
                "InstanceName": "wurong-20200915-ls01",
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "AppId": 1257780094,
                "Uin": "100007799884",
                "VpcId": "vpc-ck9abamb",
                "SubnetId": "subnet-gmmt588q",
                "Status": 1,
                "ChargeType": "POSTPAID_BY_HOUR",
                "ChargePeriod": 0,
                "RenewFlag": "",
                "NodeType": "LOGSTASH.S1.MEDIUM4",
                "NodeNum": 5,
                "DiskType": "CLOUD_SSD",
                "DiskSize": 100,
                "LogstashVersion": "6.8.13",
                "YMLConfig": "",
                "LicenseType": "xpack",
                "BindedESInstanceId": "",
                "Nodes": [
                    {
                        "NodeId": "100003160015134602",
                        "Ip": "10.0.3.136",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160015134603",
                        "Ip": "10.0.3.249",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160015279213",
                        "Ip": "10.0.3.227",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160015279214",
                        "Ip": "10.0.3.248",
                        "Port": 9600
                    },
                    {
                        "NodeId": "100003160015279215",
                        "Ip": "10.0.3.83",
                        "Port": 9600
                    }
                ],
                "ExtendedFiles": [
                    {
                        "Name": "xx",
                        "Size": 1
                    }
                ],
                "CpuNum": 1,
                "MemSize": 1,
                "OperationDuration": {
                    "TimeStart": "xx",
                    "TimeZone": "xx",
                    "Periods": [
                        1
                    ],
                    "TimeEnd": "xx"
                },
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CreateTime": "2020-09-15 14:29:06",
                "UpdateTime": "2020-09-15 15:28:27",
                "Deadline": "2017-12-04 00:00:00"
            }
        ],
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccxxxxxx"
    }
}
```

