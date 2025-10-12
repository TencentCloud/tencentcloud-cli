**Example 1: 查询数据源列表**



Input: 

```
tccli wedata ListDataSources --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Category": "DB",
                    "CreateTime": "2025-09-03 00:11:03",
                    "CreateUser": "100028579606",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "mysql_2",
                    "Id": 62268,
                    "ModifyTime": "2025-09-03 00:11:03",
                    "ModifyUser": "100028579606",
                    "Name": "mysql_2",
                    "ProdConProperties": "{\"newType\":1,\"connectType\":\"public\",\"ip\":\"1.1.1.1\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://1.1.1.1:1111/database\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"1111\",\"regionAbbr\":\"gz\",\"vpcId\":\"vpc-ds5rpnxh\",\"passwordEncrypt\":\"e3e5315db835fc7f7c70896fa3553d81\",\"region\":\"ap-guangzhou\",\"db\":\"database\",\"username\":\"aaaa\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "MYSQL"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-09-03 00:09:19",
                    "CreateUser": "100028579606",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "mysql_1",
                    "Id": 62267,
                    "ModifyTime": "2025-09-03 00:09:19",
                    "ModifyUser": "100028579606",
                    "Name": "mysql_1",
                    "ProdConProperties": "{\"newType\":1,\"connectType\":\"public\",\"ip\":\"1.1.1.1\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://1.1.1.1:1111/database\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"1111\",\"regionAbbr\":\"gz\",\"vpcId\":\"vpc-ds5rpnxh\",\"passwordEncrypt\":\"e3e5315db835fc7f7c70896fa3553d81\",\"region\":\"ap-guangzhou\",\"db\":\"database\",\"username\":\"aaaa\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "MYSQL"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-09-02 23:58:49",
                    "CreateUser": "100029411056",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "mysql_22",
                    "Id": 62266,
                    "ModifyTime": "2025-09-02 23:58:49",
                    "ModifyUser": "100029411056",
                    "Name": "mysql_22",
                    "ProdConProperties": "{\"newType\":1,\"advanceParams\":[],\"connectType\":\"public\",\"ip\":\"1.1.1.1\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://1.1.1.1:1111/database\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"1111\",\"regionAbbr\":\"sh\",\"vpcId\":\"vpc-3grmb0p6\",\"passwordEncrypt\":\"dd97cae55f379e13a799657430898d93\",\"region\":\"ap-shanghai\",\"db\":\"database\",\"username\":\"root\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "MYSQL"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-09-02 23:41:53",
                    "CreateUser": "100029411056",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "mysql_11",
                    "Id": 62265,
                    "ModifyTime": "2025-09-02 23:41:53",
                    "ModifyUser": "100029411056",
                    "Name": "mysql_11",
                    "ProdConProperties": "{\"newType\":1,\"advanceParams\":[],\"connectType\":\"public\",\"ip\":\"1.1.1.1\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://1.1.1.1:1111/database\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"1111\",\"regionAbbr\":\"gz\",\"vpcId\":\"vpc-ds5rpnxh\",\"passwordEncrypt\":\"dd97cae55f379e13a799657430898d93\",\"region\":\"ap-guangzhou\",\"db\":\"database\",\"username\":\"root\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "MYSQL"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-08-25 19:53:04",
                    "CreateUser": "100028644302",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "spark_job_dlc",
                    "Id": 62260,
                    "ModifyTime": "2025-08-25 19:53:04",
                    "ModifyUser": "100028644302",
                    "Name": "spark_job_dlc",
                    "ProdConProperties": "{\"newType\":0,\"datasourceConnectionName\":\"DataLakeCatalog\",\"connectType\":\"cdb\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"datasource_connection_name\":\"DataLakeCatalog\",\"type\":\"DLC\",\"authorityType\":\"true\",\"deployType\":\"INSTANCE\",\"url\":\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dBatchSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003ddataexplore_test_sparkjob\",\"vurl\":\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dBatchSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003ddataexplore_test_sparkjob\",\"dlcResources\":\"[{\\\"ComputeResourceType\\\":\\\"spark\\\",\\\"ComputeResourceTypeDetail\\\":\\\"SparkBatch\\\",\\\"ComputeResource\\\":\\\"dataexplore_test_sparkjob\\\",\\\"Url\\\":\\\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dBatchSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003ddataexplore_test_sparkjob\\\",\\\"Mapping\\\":null,\\\"EngineGeneration\\\":\\\"SuperSQL\\\",\\\"Resource\\\":null,\\\"EngineType\\\":null}]\",\"dlcJwtSecret\":\"tbds@2022\",\"password\":\"\",\"vpcTenantId\":\"1315051789\",\"regionAbbr\":\"bj\",\"region\":\"ap-beijing\",\"dlcGatewayUrl\":\"https://wedata-api-fusion-dev.cloud.tencent.com\",\"db\":\"yauluo_test_addel\",\"dlcRegion\":\"ap-beijing\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "DLC"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-08-25 19:52:13",
                    "CreateUser": "100028644302",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "standard_dlc",
                    "Id": 62259,
                    "ModifyTime": "2025-08-25 19:52:13",
                    "ModifyUser": "100028644302",
                    "Name": "standard_dlc",
                    "ProdConProperties": "{\"newType\":0,\"datasourceConnectionName\":\"DataLakeCatalog\",\"connectType\":\"cdb\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"datasource_connection_name\":\"DataLakeCatalog\",\"type\":\"DLC\",\"authorityType\":\"true\",\"deployType\":\"INSTANCE\",\"url\":\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dSparkSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003dnew_dlc_ai_spark\",\"vurl\":\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dSparkSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003dnew_dlc_ai_spark\",\"dlcResources\":\"[{\\\"ComputeResourceType\\\":\\\"spark\\\",\\\"ComputeResourceTypeDetail\\\":\\\"StandardSpark\\\",\\\"ComputeResource\\\":\\\"new_dlc_ai_spark\\\",\\\"Url\\\":\\\"jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type\\u003dSparkSQLTask\\u0026database_name\\u003dyauluo_test_addel\\u0026datasource_connection_name\\u003dDataLakeCatalog\\u0026region\\u003dap-beijing\\u0026data_engine_name\\u003dnew_dlc_ai_spark\\\",\\\"Mapping\\\":null,\\\"EngineGeneration\\\":\\\"Native\\\",\\\"Resource\\\":null,\\\"EngineType\\\":null}]\",\"dlcJwtSecret\":\"tbds@2022\",\"password\":\"\",\"vpcTenantId\":\"1315051789\",\"regionAbbr\":\"bj\",\"region\":\"ap-beijing\",\"dlcGatewayUrl\":\"https://wedata-api-fusion-dev.cloud.tencent.com\",\"db\":\"yauluo_test_addel\",\"dlcRegion\":\"ap-beijing\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "DLC"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-07-25 16:05:43",
                    "CreateUser": "100039182306",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "kyuubi_lhd_test",
                    "Id": 62189,
                    "ModifyTime": "2025-07-25 16:05:43",
                    "ModifyUser": "100039182306",
                    "Name": "kyuubi_lhd_test",
                    "ProdConProperties": "{\"newType\":0,\"instance\":\"true\",\"connectType\":\"cdb\",\"clusterDeployType\":\"CVM\",\"type\":\"Kyuubi\",\"deployType\":\"INSTANCE\",\"vurl\":\"jdbc:hive2://30.46.228.10:15678,30.46.228.10:14731,30.46.228.10:12445,30.46.228.10:15723/wedata_test;\",\"UniqSubnetId\":\"subnet-kp6lkzlp\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"regionAbbr\":\"bj\",\"vpcId\":\"vpc-a2yxjvxq\",\"host\":\"172.16.0.162:10009,172.16.0.233:10009,172.16.0.251:10009,172.16.1.49:10009\",\"authentication\":\"none\",\"ip\":\"172.16.0.162\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"authorityType\":\"true\",\"url\":\"jdbc:hive2://172.16.0.162:10009,172.16.0.233:10009,172.16.0.251:10009,172.16.1.49:10009/wedata_test;\",\"VgwType\":\"0\",\"vhost\":\"30.46.228.10:15678,30.46.228.10:14731,30.46.228.10:12445,30.46.228.10:15723\",\"instanceid\":\"emr-dbcygrxq\",\"instancename\":\"测试专用_AUTOTEST_勿删\",\"port\":\"10009\",\"passwordEncrypt\":\"60c0fe5c0e357bf8aa0b4d1f6ebd973e\",\"region\":\"ap-beijing\",\"kyUrl\":\"jdbc:hive2://172.16.0.162:10009,172.16.0.233:10009,172.16.0.251:10009,172.16.1.49:10009/wedata_test;\",\"db\":\"wedata_test\",\"username\":\"wedata\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "Kyuubi"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-07-22 21:51:51",
                    "CreateUser": "100038739801",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "silen_mysql",
                    "Id": 62175,
                    "ModifyTime": "2025-07-22 21:51:51",
                    "ModifyUser": "100038739801",
                    "Name": "silen_mysql",
                    "ProdConProperties": "{\"newType\":1,\"advanceParams\":[],\"vport\":\"63925\",\"connectType\":\"public\",\"ip\":\"43.137.113.95\",\"publicPort\":\"63925\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"publicIp\":\"43.137.113.95\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_PUBLICDB\",\"url\":\"jdbc:mysql://43.137.113.95:63925/wedataDB\",\"vurl\":\"jdbc:mysql://43.137.113.95:63925/wedataDB\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"63925\",\"passwordEncrypt\":\"0b3b23b8affddfc907f66ff85afb5939\",\"publicUrl\":\"jdbc:mysql://43.137.113.95:63925/wedataDB\",\"vip\":\"43.137.113.95\",\"db\":\"wedataDB\",\"username\":\"wedata\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "MYSQL"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-07-10 21:57:04",
                    "CreateUser": "100041133436",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "starrocks-xzp",
                    "Id": 62145,
                    "ModifyTime": "2025-07-10 21:57:04",
                    "ModifyUser": "100041133436",
                    "Name": "starrocks-xzp",
                    "ProdConProperties": "{\"newType\":0,\"vport\":\"18703\",\"connectType\":\"public\",\"ip\":\"172.16.7.233\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"type\":\"StarRocks\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://172.16.7.233:9030/test\",\"vurl\":\"jdbc:mysql://30.46.228.10:18703/test\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"beUrls\":\"172.16.7.233:8030\",\"port\":\"9030\",\"regionAbbr\":\"bj\",\"vpcId\":\"vpc-a2yxjvxq\",\"passwordEncrypt\":\"d34baadacea36e76d4a54d603e071499\",\"region\":\"ap-beijing\",\"vip\":\"30.46.228.10\",\"db\":\"test\",\"username\":\"root\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "StarRocks"
                },
                {
                    "Category": "DB",
                    "CreateTime": "2025-07-02 22:23:51",
                    "CreateUser": "100042282926",
                    "Description": null,
                    "DevConProperties": null,
                    "DisplayName": "bbk_cdb_test2",
                    "Id": 62142,
                    "ModifyTime": "2025-07-02 22:23:51",
                    "ModifyUser": "100042282926",
                    "Name": "bbk_cdb_test2",
                    "ProdConProperties": "{\"newType\":0,\"advanceParams\":[],\"instance\":\"true\",\"vport\":\"14836\",\"connectType\":\"cdb\",\"type\":\"TDSQLC\",\"deployType\":\"INSTANCE\",\"vurl\":\"jdbc:mysql://30.46.228.10:14836/bbk\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"regionAbbr\":\"bj\",\"vpcId\":\"vpc-a2yxjvxq\",\"vip\":\"30.46.228.10\",\"ip\":\"172.16.0.16\",\"cosBucketName\":\"wedata-fusion-dev-1257305158\",\"cosRegion\":\"ap-nanjing\",\"authorityType\":\"true\",\"version\":\"8.0\",\"url\":\"jdbc:mysql://172.16.0.16:3306/bbk\",\"VgwType\":\"0\",\"instanceid\":\"cynosdbmysql-ins-d6b01mhr\",\"instancename\":\"cynosdbmysql-ins-d6b01mhr\",\"port\":\"3306\",\"passwordEncrypt\":\"f428e1ed1fd4ea3402289ba32f80cbc6\",\"region\":\"ap-beijing\",\"db\":\"bbk\",\"username\":\"root\"}",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "[调度dev验证项目_new2]",
                    "Type": "TDSQLC"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 156,
            "TotalPageNumber": null
        },
        "RequestId": "ccd89c16-fee9-4c7d-ae08-5402f34a2374"
    }
}
```

