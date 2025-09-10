**Example 1: 查询Datahub连接源列表**

查询Datahub连接源列表

Input: 

```
tccli ckafka DescribeConnectResources --cli-unfold-argument  \
    --Limit 20 \
    --Type KAFKA \
    --SearchWord mytest \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ConnectResourceList": [
                {
                    "ResourceId": "resource-y9v8e3bl",
                    "ResourceName": "mytest",
                    "Description": "",
                    "Status": 1,
                    "CreateTime": "2024-12-04 16:21:08",
                    "ErrorMessage": "RUNNING",
                    "CurrentStep": "FINISH",
                    "DatahubTaskCount": 0,
                    "TaskProgress": 36,
                    "StepList": [
                        "WAIT_CREATE_PRIVATELINK",
                        "WAIT_CONNECT_PORT",
                        "WAIT_CONNECT_RESOURCE"
                    ],
                    "Type": "KAFKA",
                    "MongoDBConnectParam": null,
                    "EsConnectParam": null,
                    "ClickHouseConnectParam": null,
                    "DtsConnectParam": null,
                    "MySQLConnectParam": null,
                    "MqttConnectParam": null,
                    "PostgreSQLConnectParam": null,
                    "MariaDBConnectParam": null,
                    "SQLServerConnectParam": null,
                    "CtsdbConnectParam": null,
                    "DorisConnectParam": null,
                    "KafkaConnectParam": {
                        "Region": "ap-guangzhou",
                        "BrokerAddress": "11.135.14.76:8568",
                        "SelfBuilt": false,
                        "Resource": "ckafka-wdvgwwx2",
                        "IsUpdate": null
                    }
                }
            ]
        },
        "RequestId": "21de50a2-3626-4194-a60b-0741e396f368"
    }
}
```

