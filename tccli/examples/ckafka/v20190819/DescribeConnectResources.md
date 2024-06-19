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
                    "ResourceId": "abc",
                    "ResourceName": "abc",
                    "Description": "abc",
                    "Type": "abc",
                    "Status": 0,
                    "CreateTime": "abc",
                    "ErrorMessage": "abc",
                    "DatahubTaskCount": 0,
                    "CurrentStep": "abc",
                    "TaskProgress": 0,
                    "StepList": [
                        "abc"
                    ],
                    "DtsConnectParam": {
                        "Port": 0,
                        "GroupId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "IsUpdate": true,
                        "Topic": "abc"
                    },
                    "MongoDBConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "SelfBuilt": true,
                        "IsUpdate": true
                    },
                    "EsConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "SelfBuilt": true,
                        "IsUpdate": true
                    },
                    "ClickHouseConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "SelfBuilt": true,
                        "IsUpdate": true
                    },
                    "MySQLConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "IsUpdate": true,
                        "ClusterId": "abc",
                        "SelfBuilt": true
                    },
                    "PostgreSQLConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "ClusterId": "abc",
                        "IsUpdate": true,
                        "SelfBuilt": true
                    },
                    "MariaDBConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "IsUpdate": true
                    },
                    "SQLServerConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "IsUpdate": true
                    },
                    "CtsdbConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc"
                    },
                    "DorisConnectParam": {
                        "Port": 0,
                        "ServiceVip": "abc",
                        "UniqVpcId": "abc",
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "IsUpdate": true,
                        "SelfBuilt": true,
                        "BePort": 0
                    },
                    "KafkaConnectParam": {
                        "Resource": "abc",
                        "SelfBuilt": true,
                        "IsUpdate": true,
                        "BrokerAddress": "abc",
                        "Region": "abc"
                    },
                    "MqttConnectParam": {
                        "UserName": "abc",
                        "Password": "abc",
                        "Resource": "abc",
                        "UniqVpcId": "abc",
                        "SelfBuilt": true,
                        "IsUpdate": true,
                        "Region": "abc"
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

