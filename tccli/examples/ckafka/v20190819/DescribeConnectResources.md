**Example 1: 查询Datahub连接源列表**

查询Datahub连接源列表

Input: 

```
tccli ckafka DescribeConnectResources --cli-unfold-argument  \
    --Limit 0 \
    --Type xxx \
    --SearchWord xxx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "ConnectResourceList": [
                {
                    "Status": 0,
                    "ResourceName": "xxx",
                    "Description": "xxx",
                    "ResourceId": "resource-xxx",
                    "DtsConnectParam": {
                        "Topic": "xxx",
                        "UserName": "xxx",
                        "Resource": "xxx",
                        "GroupId": "xxx",
                        "Password": "xxx",
                        "Port": 0
                    },
                    "MySQLConnectParam": null,
                    "MongoDBConnectParam": null,
                    "EsConnectParam": null,
                    "PostgreSQLConnectParam": null,
                    "ClickHouseConnectParam": null,
                    "SQLServerConnectParam": null,
                    "CurrentStep": "FINISH",
                    "CtsdbConnectParam": null,
                    "ErrorMessage": "RUNNING",
                    "MariaDBConnectParam": null,
                    "DorisConnectParam": null,
                    "Type": "",
                    "DatahubTaskCount": 0,
                    "CreateTime": "xxx"
                }
            ]
        },
        "RequestId": "xxx"
    }
}
```

