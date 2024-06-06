**Example 1: 查询所有实例列表**

按指定分页查询实例列表

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
                "AppId": 123456789,
                "AutoRenew": 1,
                "CreateTime": "2022-03-16 18:12:10",
                "DBCharset": "UTF8",
                "DBEngine": "postgresql",
                "DBEngineConfig": "",
                "DBInstanceClass": "cdb.pg.ts1.8g",
                "DBInstanceCpu": 4,
                "DBInstanceId": "postgres-xxxxxx",
                "DBInstanceMemory": 8,
                "DBInstanceName": "test",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "xx.xx.xx.xx",
                        "NetType": "private",
                        "Port": 5432,
                        "ProtocolType": "postgresql",
                        "Status": "opened",
                        "SubnetId": "subnet-xxxx",
                        "VpcId": "vpc-xxxx"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "NetType": "public",
                        "Port": 0,
                        "ProtocolType": "",
                        "Status": "initing",
                        "SubnetId": "",
                        "VpcId": ""
                    }
                ],
                "DBInstanceStatus": "running",
                "DBInstanceStorage": 20,
                "DBInstanceType": "primary",
                "DBInstanceVersion": "standard",
                "DBKernelVersion": "v13.3_r1.1",
                "DBMajorVersion": "13",
                "DBNodeSet": [
                    {
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-6"
                    },
                    {
                        "Role": "Standby",
                        "Zone": "ap-guangzhou-6"
                    }
                ],
                "DBVersion": "13.3",
                "ExpireTime": "2023-04-16 18:14:49",
                "IsSupportTDE": 0,
                "IsolatedTime": "0000-00-00 00:00:00",
                "MasterDBInstanceId": "",
                "NetworkAccessList": null,
                "OfflineTime": "0001-01-08 00:00:00",
                "PayType": "prepaid",
                "ProjectId": 0,
                "ReadOnlyInstanceNum": 0,
                "Region": "ap-guangzhou",
                "StatusInReadonlyGroup": "",
                "SubnetId": "subnet-xxxx",
                "SupportIpv6": 0,
                "TagList": [
                    {
                        "TagKey": "tag_key_test",
                        "TagValue": "tag_value_test"
                    }
                ],
                "Type": "TS85",
                "Uid": 1234,
                "UpdateTime": "2023-03-15 17:31:58",
                "VpcId": "vpc-xxxx",
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RequestId": "d849664a-191c-48bf-b42f-444caa189557"
    }
}
```

**Example 2: 根据实例ID查询实例信息**

例如：查询实例ID为postgres-xxxxx的实例信息

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Values postgres-xxxxx \
    --Filters.0.Name db-instance-id \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DBInstanceSet": [
            {
                "AppId": 123456789,
                "AutoRenew": 1,
                "CreateTime": "2022-03-16 18:12:10",
                "DBCharset": "UTF8",
                "DBEngine": "postgresql",
                "DBEngineConfig": "",
                "DBInstanceClass": "cdb.pg.ts1.8g",
                "DBInstanceCpu": 4,
                "DBInstanceId": "postgres-xxxxx",
                "DBInstanceMemory": 8,
                "DBInstanceName": "test",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "xx.xx.xx.xx",
                        "NetType": "private",
                        "Port": 5432,
                        "ProtocolType": "postgresql",
                        "Status": "opened",
                        "SubnetId": "subnet-xxxx",
                        "VpcId": "vpc-xxxx"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "NetType": "public",
                        "Port": 0,
                        "ProtocolType": "",
                        "Status": "initing",
                        "SubnetId": "",
                        "VpcId": ""
                    }
                ],
                "DBInstanceStatus": "running",
                "DBInstanceStorage": 20,
                "DBInstanceType": "primary",
                "DBInstanceVersion": "standard",
                "DBKernelVersion": "v13.3_r1.1",
                "DBMajorVersion": "13",
                "DBNodeSet": [
                    {
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-6"
                    },
                    {
                        "Role": "Standby",
                        "Zone": "ap-guangzhou-6"
                    }
                ],
                "DBVersion": "13.3",
                "ExpireTime": "2023-04-16 18:14:49",
                "IsSupportTDE": 0,
                "IsolatedTime": "0000-00-00 00:00:00",
                "MasterDBInstanceId": "",
                "NetworkAccessList": null,
                "OfflineTime": "0001-01-08 00:00:00",
                "PayType": "prepaid",
                "ProjectId": 0,
                "ReadOnlyInstanceNum": 0,
                "Region": "ap-guangzhou",
                "StatusInReadonlyGroup": "",
                "SubnetId": "subnet-xxxx",
                "SupportIpv6": 0,
                "TagList": [
                    {
                        "TagKey": "tag_key_test",
                        "TagValue": "tag_value_test"
                    }
                ],
                "Type": "TS85",
                "Uid": 1234,
                "UpdateTime": "2023-03-15 17:31:58",
                "VpcId": "vpc-xxxx",
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RequestId": "d849664a-191c-48bf-b42f-444caa189557"
    }
}
```

