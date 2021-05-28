**Example 1: 查询所有实例列表**



Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DBInstanceSet": [
            {
                "Zone": "xx",
                "DBInstanceName": "xx",
                "Type": "xx",
                "ReadOnlyInstanceNum": 1,
                "MasterDBInstanceId": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "IsolatedTime": "2020-09-22 00:00:00",
                "DBVersion": "xx",
                "DBInstanceVersion": "xx",
                "AutoRenew": 1,
                "StatusInReadonlyGroup": "xx",
                "SubnetId": "xx",
                "DBInstanceMemory": 1,
                "DBInstanceType": "xx",
                "DBInstanceStatus": "xx",
                "OfflineTime": "xx",
                "Region": "xx",
                "ProjectId": 1,
                "DBInstanceNetInfo": [
                    {
                        "Status": "xx",
                        "Ip": "xx",
                        "Port": 1,
                        "NetType": "xx",
                        "Address": "xx"
                    },
                    {
                        "Status": "xx",
                        "Ip": "xx",
                        "Port": 1,
                        "NetType": "xx",
                        "Address": "xx"
                    }
                ],
                "DBInstanceStorage": 1,
                "Uid": 1,
                "DBCharset": "xx",
                "DBInstanceId": "xx",
                "PayType": "xx",
                "ExpireTime": "2020-09-22 00:00:00",
                "SupportIpv6": 1,
                "AppId": 1,
                "DBInstanceClass": "xx",
                "CreateTime": "2020-09-22 00:00:00",
                "DBInstanceCpu": 1,
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            },
            {
                "Zone": "xx",
                "DBInstanceName": "xx",
                "Type": "xx",
                "ReadOnlyInstanceNum": 1,
                "UpdateTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "IsolatedTime": "2020-09-22 00:00:00",
                "DBVersion": "xx",
                "DBInstanceVersion": "xx",
                "AutoRenew": 1,
                "ProjectId": 1,
                "SubnetId": "xx",
                "DBInstanceMemory": 1,
                "DBInstanceType": "xx",
                "DBInstanceStatus": "xx",
                "OfflineTime": "xx",
                "Region": "xx",
                "StatusInReadonlyGroup": "xx",
                "MasterDBInstanceId": "xx",
                "DBInstanceNetInfo": [
                    {
                        "Status": "xx",
                        "Ip": "xx",
                        "Port": 1,
                        "NetType": "xx",
                        "Address": "xx"
                    },
                    {
                        "Status": "xx",
                        "Ip": "xx",
                        "Port": 1,
                        "NetType": "xx",
                        "Address": "xx"
                    }
                ],
                "DBInstanceStorage": 1,
                "Uid": 1,
                "DBCharset": "xx",
                "DBInstanceId": "xx",
                "PayType": "xx",
                "ExpireTime": "2020-09-22 00:00:00",
                "SupportIpv6": 1,
                "AppId": 1,
                "DBInstanceClass": "xx",
                "CreateTime": "2020-09-22 00:00:00",
                "DBInstanceCpu": 1,
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 根据实例ID查询实例信息**

例如：查询实例ID为postgres-6bwgamo3的实例信息

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name db-instance-id \
    --Filters.0.Values postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "d849664a-191c-48bf-b42f-444caa189557",
        "TotalCount": 2,
        "DBInstanceSet": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "AppId": 100000000,
                "Uid": 1000001,
                "ProjectId": 0,
                "VpcId": "",
                "SubnetId": "",
                "Type": 1,
                "DBInstanceId": "postgres-6bwgamo3",
                "MasterDBInstanceId": "",
                "DBInstanceName": "test",
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
                        "Ip": "xxxx",
                        "Port": 5432,
                        "Status": "opened",
                        "NetType": "inner"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "0",
                        "NetType": "public"
                    }
                ],
                "DBCharset": "UTF8",
                "DBVersion": "9.5.4",
                "CreateTime": "2017-12-28 19:23:19",
                "UpdateTime": "2018-01-18 15:54:32",
                "ExpireTime": "2018-01-28 19:23:23",
                "IsolatedTime": "0000-00-00 00:00:00",
                "OfflineTime": "2019-12-28 19:23:19",
                "StatusInReadonlyGroup": "ruuning",
                "ReadOnlyInstanceNum": 1,
                "PayType": "prepaid",
                "AutoRenew": 1,
                "SupportIpv6": 0,
                "TagList": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "v1"
                    }
                ]
            }
        ]
    }
}
```

