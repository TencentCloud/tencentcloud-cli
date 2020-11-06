**Example 1: 查询实例的详细信息**



Input: 

```
tccli postgres DescribeDBInstanceAttribute --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3
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
            "ProjectId": 0,
            "VpcId": "",
            "SubnetId": "",
            "DBInstanceId": "postgres-6bwgamo3",
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
                    "Ip": "xxxxx",
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
    }
}
```

