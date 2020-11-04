**Example 1: 查询所有实例列表**



Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a6e3c73c-6810-42c2-842e-fa759ce52fa0",
        "TotalCount": 2,
        "DBInstanceSet": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "AppId": 251000710,
                "ProjectId": 0,
                "VpcId": "",
                "SubnetId": "",
                "DBInstanceId": "postgres-6bwgamo3",
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
                        "Ip": "10.66.187.1",
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
                "PayType": "prepaid",
                "AutoRenew": false
            },
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "AppId": 251000710,
                "ProjectId": 0,
                "VpcId": "",
                "SubnetId": "",
                "DBInstanceId": "postgres-1e2srvtt",
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
                        "Ip": "10.66.195.51",
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
                "CreateTime": "2017-12-28 19:50:15",
                "UpdateTime": "2018-01-19 10:34:21",
                "ExpireTime": "2018-01-28 19:50:17",
                "IsolatedTime": "0000-00-00 00:00:00",
                "PayType": "prepaid",
                "AutoRenew": false
            }
        ]
    }
}
```

**Example 2: 根据实例ID查询实例信息**

例如：查询实例ID为postgres-6bwgamo3的实例信息

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10\
    --Offset 0\
    --Filters.0.Name db-instance-id\
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
                "ProjectId": 0,
                "VpcId": "",
                "SubnetId": "",
                "DBInstanceId": "postgres-6bwgamo3",
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
                "PayType": "prepaid",
                "AutoRenew": false
            }
        ]
    }
}
```

