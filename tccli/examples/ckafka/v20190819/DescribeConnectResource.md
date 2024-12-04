**Example 1: 查询Datahub连接源**



Input: 

```
tccli ckafka DescribeConnectResource --cli-unfold-argument  \
    --ResourceId reource-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-y9v8e3bl",
            "ResourceName": "mytest",
            "Type": "KAFKA",
            "Description": "",
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
            },
            "Status": 1,
            "CreateTime": "2024-12-04 16:21:08",
            "ErrorMessage": "RUNNING",
            "CurrentStep": "FINISH",
            "StepList": [
                "WAIT_CREATE_PRIVATELINK",
                "WAIT_CONNECT_PORT",
                "WAIT_CONNECT_RESOURCE"
            ]
        },
        "RequestId": "4cd38c99-9e9a-4a2d-8641-fa7c4015f764"
    }
}
```

