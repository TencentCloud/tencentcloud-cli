**Example 1: 查询DataEngines信息列表**

查询DataEngines信息列表

Input: 

```
tccli dlc DescribeDataEngines --cli-unfold-argument  \
    --Offset 1 \
    --Filters.0.Name engine-type \
    --Filters.0.Values spark \
    --SortBy create-time \
    --Sorting desc \
    --Limit 10 \
    --DatasourceConnectionName default-network-3 \
    --ExcludePublicEngine False \
    --AccessTypes USE \
    --EngineExecType BATCH \
    --EngineType spark \
    --DatasourceConnectionNameSet net1111 \
    --EngineGeneration Native \
    --EngineTypeDetail SparkSQL
```

Output: 
```
{
    "Response": {
        "DataEngines": [
            {
                "DataEngineName": "",
                "QuotaId": "",
                "EngineType": "",
                "ClusterType": "",
                "State": 0,
                "CreateTime": 0,
                "UpdateTime": 0,
                "Size": 0,
                "Mode": 0,
                "MinClusters": 0,
                "MaxClusters": 0,
                "AutoResume": false,
                "SpendAfter": 0,
                "CidrBlock": "",
                "DefaultDataEngine": false,
                "Message": "",
                "DataEngineId": "",
                "SubAccountUin": "",
                "ExpireTime": "",
                "IsolatedTime": "",
                "ReversalTime": "",
                "UserAlias": "",
                "TagList": [
                    {
                        "TagKey": "",
                        "TagValue": ""
                    }
                ],
                "Permissions": [
                    ""
                ],
                "AutoSuspend": false,
                "CrontabResumeSuspend": 0,
                "CrontabResumeSuspendStrategy": {
                    "ResumeTime": "",
                    "SuspendTime": "",
                    "SuspendStrategy": 0
                },
                "EngineExecType": "",
                "RenewFlag": 0,
                "AutoSuspendTime": 0,
                "NetworkConnectionSet": [
                    {
                        "Id": 0,
                        "AssociateId": "",
                        "HouseId": "",
                        "DatasourceConnectionId": "",
                        "State": 0,
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Appid": 0,
                        "HouseName": "",
                        "DatasourceConnectionName": "",
                        "NetworkConnectionType": 0,
                        "Uin": "",
                        "SubAccountUin": "",
                        "NetworkConnectionDesc": "",
                        "DatasourceConnectionVpcId": "",
                        "DatasourceConnectionSubnetId": "",
                        "DatasourceConnectionCidrBlock": "",
                        "DatasourceConnectionSubnetCidrBlock": ""
                    }
                ],
                "UiURL": "",
                "ResourceType": "",
                "ImageVersionId": "",
                "ChildImageVersionId": "",
                "ImageVersionName": "",
                "StartStandbyCluster": false,
                "ElasticSwitch": false,
                "ElasticLimit": 0,
                "DefaultHouse": false,
                "MaxConcurrency": 0,
                "TolerableQueueTime": 0,
                "UserAppId": 0,
                "UserUin": "",
                "SessionResourceTemplate": {
                    "DriverSize": "",
                    "ExecutorSize": "",
                    "ExecutorNums": 0,
                    "ExecutorMaxNumbers": 0
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "896387ab-35dc-4f14-b086-ed0e8ca050d9"
    }
}
```

**Example 2: 查询DataEngines信息列表test**

查询DataEngines信息列表test

Input: 

```
tccli dlc DescribeDataEngines --cli-unfold-argument  \
    --Offset 1 \
    --SortBy create-time \
    --Sorting desc \
    --Limit 1 \
    --DatasourceConnectionName DataLakeCatalog \
    --AccessTypes USE MODIFY OPERATE MONITOR DELETE \
    --EngineExecType BATCH \
    --EngineType spark \
    --EngineGeneration Native \
    --EngineTypeDetail StandardSpark
```

Output: 
```
{
    "Response": {
        "DataEngines": [
            {
                "AccessInfos": [
                    {
                        "AccessConnectionInfos": [
                            "jdbc:hive2://192.*.*.*:*/?spark.engine=dlc-spark;spark.resourcegroup={ResourceGroupName};secretkey={SecretKey};secretid={SecretId};region=ap-beijing;kyuubi.engine.type=SPARK_SQL;kyuubi.engine.share.level=ENGINE"
                        ],
                        "AccessType": "HiveJDBC"
                    },
                    {
                        "AccessConnectionInfos": [
                            "jdbc:dlc:dlc.tencentcloudapi.com?task_type=SparkSQLTask&database_name={DatabaseName}&datasource_connection_name=DataLakeCatalog&region=ap-beijing-&data_engine_name=dlc-spark&resource_group_name={ResourceGroupName}"
                        ],
                        "AccessType": "DLCJDBC"
                    }
                ],
                "AutoAuthorization": true,
                "AutoResume": false,
                "AutoSuspend": false,
                "AutoSuspendTime": 10,
                "ChildImageVersionId": "681fab43-a79c-42ec-9c7b-42917af33611",
                "CidrBlock": "10.*.*.*/16",
                "ClusterType": "spark_cu",
                "CreateTime": 1735872007,
                "CrontabResumeSuspend": 0,
                "CrontabResumeSuspendStrategy": {
                    "ResumeTime": "",
                    "SuspendStrategy": 0,
                    "SuspendTime": ""
                },
                "DataEngineId": "DataEngine-houseid1",
                "DataEngineName": "dlc-spark",
                "DefaultDataEngine": false,
                "DefaultHouse": false,
                "ElasticLimit": 0,
                "ElasticSwitch": false,
                "EngineExecType": "BATCH",
                "EngineGeneration": "Native",
                "EngineNetworkId": "DataEngine-Network-networkid",
                "EngineNetworkName": "net_test",
                "EngineResourceGroupCount": 4,
                "EngineResourceUsedCU": 0,
                "EngineType": "spark",
                "EngineTypeDetail": "StandardSpark",
                "ExpireTime": "0",
                "GatewayId": "",
                "GatewayState": 0,
                "ImageVersionId": "c3a40d9a-f5fe-40ac-9c17-16fed3fd2644",
                "ImageVersionName": "Standard-S 1.1",
                "IsAIEngine": 1,
                "IsAIGateway": false,
                "IsPoolMode": null,
                "IsSupportAI": true,
                "IsolatedTime": "0",
                "MaxClusters": 1,
                "MaxConcurrency": 5,
                "Message": "",
                "MinClusters": 1,
                "Mode": 1,
                "NetworkConnectionSet": [],
                "Permissions": [
                    "USE",
                    "MODIFY",
                    "OPERATE",
                    "MONITOR",
                    "DELETE"
                ],
                "QuotaId": "",
                "RenewFlag": 0,
                "ResourceType": "Standard_CU",
                "ReversalTime": "0",
                "SessionResourceTemplate": {
                    "DriverSize": "large",
                    "ExecutorMaxNumbers": 3,
                    "ExecutorNums": 3,
                    "ExecutorSize": "large"
                },
                "Size": 16,
                "SpendAfter": 0,
                "StartStandbyCluster": false,
                "State": 2,
                "SubAccountUin": "100013032040",
                "TagList": [],
                "TolerableQueueTime": 0,
                "UiURL": "-1",
                "UpdateTime": 1735265761,
                "UserAlias": "1000****2040",
                "UserAppId": "1301234123",
                "UserUin": "1000****117"
            }
        ],
        "RequestId": "edfbd22e-4779-446a-9b2f-288cad2ba0e2",
        "TotalCount": 1
    }
}
```

