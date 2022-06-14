**Example 1: 查询实例的详细信息**



Input: 

```
tccli postgres DescribeDBInstanceAttribute --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DBInstance": {
            "Region": "ap-guangzhou",
            "Zone": "ap-guangzhou-2",
            "AppId": 100000000,
            "Uid": 1000001,
            "ProjectId": 0,
            "VpcId": "vpc-xxxxxxxx",
            "SubnetId": "subnet-xxxxxxxx",
            "DBInstanceId": "postgres-xxxxxxxx",
            "MasterDBInstanceId": "postgres-xxxxxxxx",
            "Type": 1,
            "DBInstanceName": "未命名",
            "DBInstanceStatus": "running",
            "DBInstanceMemory": 4,
            "DBInstanceStorage": 20,
            "DBInstanceCpu": 2,
            "DBInstanceClass": "cdb.pg.z1.4g",
            "DBInstanceType": "primary",
            "DBInstanceVersion": "standard",
            "DBInstanceNetInfo": [
                {
                    "Address": "",
                    "Ip": "10.10.10.220",
                    "Port": 5432,
                    "Status": "opened",
                    "NetType": "private",
                    "VpcId": "vpc-xxxxxxxx",
                    "SubnetId": "subnet-xxxxxxxx"
                },
                {
                    "Address": "",
                    "Ip": "",
                    "Port": 0,
                    "Status": "initing",
                    "NetType": "public",
                    "VpcId": "",
                    "SubnetId": ""
                }
            ],
            "DBCharset": "UTF8",
            "IsSupportTDE": 0,
            "DBVersion": "10.4",
            "DBMajorVersion": "10",
            "DBKernelVersion": "v10.4_r1.0",
            "CreateTime": "2017-12-28 19:23:19",
            "UpdateTime": "2018-01-18 15:54:32",
            "ExpireTime": "2018-01-28 19:23:23",
            "IsolatedTime": "0000-00-00 00:00:00",
            "OfflineTime": "2019-12-28 19:23:19",
            "PayType": "prepaid",
            "AutoRenew": 1,
            "ReadOnlyInstanceNum": 1,
            "StatusInReadonlyGroup": "running",
            "SupportIpv6": 0,
            "TagList": [
                {
                    "TagKey": "tag1",
                    "TagValue": "v1"
                }
            ],
            "NetworkAccessList": [],
            "DBNodeSet": [
                {
                    "Role": "Primary",
                    "Zone": "ap-guangzhou-2"
                },
                {
                    "Role": "Standby",
                    "Zone": "ap-guangzhou-3"
                }
            ]
        }
    }
}
```

