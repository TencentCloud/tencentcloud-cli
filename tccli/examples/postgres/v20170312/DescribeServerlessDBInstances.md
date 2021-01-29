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
                "DBInstanceId": "postgres-gqmunix5",
                "DBInstanceName": "anita_10",
                "DBInstanceStatus": "initing",
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "ProjectId": 0,
                "VpcId": "vpc-0mocsnzb",
                "SubnetId": "subnet-mutl5yka",
                "DBCharset": "UTF8",
                "DBVersion": "10.4",
                "CreateTime": "2020-03-20 12:19:14",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "opened",
                        "NetType": "private"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "0",
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

