**Example 1: test**



Input: 

```
tccli dlc DescribeDatasourceConnection --cli-unfold-argument  \
    --DatasourceConnectionIds abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0 \
    --SortBy abc \
    --Sorting abc \
    --StartTime abc \
    --EndTime abc \
    --DatasourceConnectionNames abc \
    --DatasourceConnectionTypes abc \
    --HiveVersion abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ConnectionSet": [
            {
                "Id": 0,
                "DatasourceConnectionId": "abc",
                "DatasourceConnectionName": "abc",
                "DatasourceConnectionDesc": "abc",
                "DatasourceConnectionType": "abc",
                "DatasourceConnectionConfig": {
                    "Mysql": {
                        "JdbcUrl": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        },
                        "DbName": "abc",
                        "InstanceId": "abc",
                        "InstanceName": "abc"
                    },
                    "Hive": {
                        "MetaStoreUrl": "abc",
                        "Type": "abc",
                        "User": "abc",
                        "HighAvailability": true,
                        "BucketUrl": "abc",
                        "HdfsProperties": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        },
                        "Mysql": {
                            "JdbcUrl": "abc",
                            "User": "abc",
                            "Password": "abc",
                            "Location": {
                                "VpcId": "abc",
                                "VpcCidrBlock": "abc",
                                "SubnetId": "abc",
                                "SubnetCidrBlock": "abc"
                            },
                            "DbName": "abc",
                            "InstanceId": "abc",
                            "InstanceName": "abc"
                        },
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "HiveVersion": "abc",
                        "KerberosInfo": {
                            "Krb5Conf": "abc",
                            "KeyTab": "abc",
                            "ServicePrincipal": "abc"
                        },
                        "KerberosEnable": true
                    },
                    "Kafka": {
                        "InstanceId": "abc"
                    },
                    "OtherDatasourceConnection": {
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        }
                    },
                    "PostgreSql": {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "JdbcUrl": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "DbName": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        }
                    },
                    "SqlServer": {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "JdbcUrl": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "DbName": "abc"
                    },
                    "ClickHouse": {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "JdbcUrl": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "DbName": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        }
                    },
                    "Elasticsearch": {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "DbName": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        },
                        "ServiceInfo": [
                            {
                                "Ip": "abc",
                                "Port": 0
                            }
                        ]
                    },
                    "TDSQLPostgreSql": {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "JdbcUrl": "abc",
                        "User": "abc",
                        "Password": "abc",
                        "DbName": "abc",
                        "Location": {
                            "VpcId": "abc",
                            "VpcCidrBlock": "abc",
                            "SubnetId": "abc",
                            "SubnetCidrBlock": "abc"
                        }
                    }
                },
                "State": 0,
                "Region": "abc",
                "AppId": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Message": "abc",
                "DataEngines": [
                    {
                        "DataEngineName": "abc",
                        "QuotaId": "abc",
                        "EngineType": "abc",
                        "ClusterType": "abc",
                        "State": 0,
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Size": 0,
                        "Mode": 0,
                        "MinClusters": 0,
                        "MaxClusters": 0,
                        "AutoResume": true,
                        "SpendAfter": 0,
                        "CidrBlock": "abc",
                        "DefaultDataEngine": true,
                        "Message": "abc",
                        "DataEngineId": "abc",
                        "SubAccountUin": "abc",
                        "ExpireTime": "abc",
                        "IsolatedTime": "abc",
                        "ReversalTime": "abc",
                        "UserAlias": "abc",
                        "TagList": [
                            {
                                "TagKey": "abc",
                                "TagValue": "abc"
                            }
                        ],
                        "Permissions": [
                            "abc"
                        ],
                        "AutoSuspend": true,
                        "CrontabResumeSuspend": 0,
                        "CrontabResumeSuspendStrategy": {
                            "ResumeTime": "abc",
                            "SuspendTime": "abc",
                            "SuspendStrategy": 0
                        },
                        "EngineExecType": "abc",
                        "RenewFlag": 0,
                        "AutoSuspendTime": 0,
                        "NetworkConnectionSet": [
                            {
                                "Id": 0,
                                "AssociateId": "abc",
                                "HouseId": "abc",
                                "DatasourceConnectionId": "abc",
                                "State": 0,
                                "CreateTime": 0,
                                "UpdateTime": 0,
                                "Appid": 0,
                                "HouseName": "abc",
                                "DatasourceConnectionName": "abc",
                                "NetworkConnectionType": 0,
                                "Uin": "abc",
                                "SubAccountUin": "abc",
                                "NetworkConnectionDesc": "abc",
                                "DatasourceConnectionVpcId": "abc",
                                "DatasourceConnectionSubnetId": "abc",
                                "DatasourceConnectionCidrBlock": "abc",
                                "DatasourceConnectionSubnetCidrBlock": "abc"
                            }
                        ],
                        "UiURL": "abc",
                        "ResourceType": "abc",
                        "ImageVersionId": "abc",
                        "ChildImageVersionId": "abc",
                        "ImageVersionName": "abc",
                        "StartStandbyCluster": true,
                        "ElasticSwitch": true,
                        "ElasticLimit": 0,
                        "DefaultHouse": true,
                        "MaxConcurrency": 0,
                        "TolerableQueueTime": 0,
                        "UserAppId": 0,
                        "UserUin": "abc",
                        "SessionResourceTemplate": {
                            "DriverSize": "abc",
                            "ExecutorSize": "abc",
                            "ExecutorNums": 1,
                            "ExecutorMaxNumbers": 1
                        },
                        "AutoAuthorization": true
                    }
                ],
                "UserAlias": "abc",
                "NetworkConnectionSet": [
                    {
                        "Id": 0,
                        "AssociateId": "abc",
                        "HouseId": "abc",
                        "DatasourceConnectionId": "abc",
                        "State": 0,
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Appid": 0,
                        "HouseName": "abc",
                        "DatasourceConnectionName": "abc",
                        "NetworkConnectionType": 0,
                        "Uin": "abc",
                        "SubAccountUin": "abc",
                        "NetworkConnectionDesc": "abc",
                        "DatasourceConnectionVpcId": "abc",
                        "DatasourceConnectionSubnetId": "abc",
                        "DatasourceConnectionCidrBlock": "abc",
                        "DatasourceConnectionSubnetCidrBlock": "abc"
                    }
                ],
                "ConnectivityState": 1,
                "ConnectivityTips": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

