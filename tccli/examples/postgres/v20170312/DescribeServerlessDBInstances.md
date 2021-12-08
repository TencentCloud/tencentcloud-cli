**Example 1: 查询ServerlessDB实例列表**



Input: 

```
tccli postgres DescribeServerlessDBInstances --cli-unfold-argument  \
    --Filter.0.Name "xxx", \
    --Limit 0 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DBInstanceSet": [
            {
                "DBInstanceId": "postgres-xxxxxxxx",
                "DBInstanceName": "xxx",
                "DBInstanceStatus": "running",
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "ProjectId": 0,
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "DBCharset": "UTF8",
                "DBVersion": "10",
                "DBKernelVersion": "v10.4_r1.0",
                "CreateTime": "2020-03-20 12:19:14",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "10.10.10.111",
                        "Port": 5432,
                        "Status": "opened",
                        "NetType": "private"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "initing",
                        "NetType": "public"
                    }
                ],
                "DBAccountSet": [],
                "DBDatabaseList": null
            }
        ],
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8"
    }
}
```

