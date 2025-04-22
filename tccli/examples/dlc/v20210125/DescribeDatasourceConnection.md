**Example 1: test**



Input: 

```
tccli dlc DescribeDatasourceConnection --cli-unfold-argument  \
    --DatasourceConnectionIds f329n1 \
    --Filters.0.Name filter \
    --Filters.0.Values normal \
    --Offset 0 \
    --Limit 0 \
    --SortBy time \
    --Sorting desc \
    --StartTime 2006-01-02 15:04:05 \
    --EndTime 2006-01-02 15:04:05 \
    --DatasourceConnectionNames connection_1 \
    --DatasourceConnectionTypes connection_1 \
    --HiveVersion 2.1.1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ConnectionSet": [
            {
                "Id": 0,
                "DatasourceConnectionId": "datasourceId",
                "DatasourceConnectionName": "datasourceName",
                "DatasourceConnectionDesc": "desc",
                "DatasourceConnectionType": "noraml",
                "DatasourceConnectionConfig": {
                    "Mysql": {
                        "JdbcUrl": "jdbc://xxxx:3306",
                        "User": "userName",
                        "Password": "sMKind1",
                        "Location": {
                            "VpcId": "g5i12",
                            "VpcCidrBlock": "jk09",
                            "SubnetId": "netJ098",
                            "SubnetCidrBlock": "subnet109"
                        },
                        "DbName": "dev",
                        "InstanceId": "instance2",
                        "InstanceName": "instanceName"
                    },
                    "Hive": {
                        "MetaStoreUrl": "jdbc://xxxmetasotre:3306",
                        "Type": "normal",
                        "User": "admin",
                        "HighAvailability": true,
                        "BucketUrl": "ins-1vogaxgk",
                        "HdfsProperties": "hdfs",
                        "Location": {
                            "VpcId": "JO21Ijk",
                            "VpcCidrBlock": "vpc908",
                            "SubnetId": "sub1",
                            "SubnetCidrBlock": "subblock1"
                        },
                        "Mysql": {
                            "JdbcUrl": "ins-1vogaxgk",
                            "Password": "admin",
                            "Location": {
                                "VpcId": "877d6fb03",
                                "VpcCidrBlock": "77d6fb03",
                                "SubnetId": "3c140219",
                                "SubnetCidrBlock": "b241-90"
                            },
                            "DbName": "db1",
                            "InstanceId": "3c103",
                            "InstanceName": "417d6fb03"
                        },
                        "InstanceId": "77d6fb03",
                        "InstanceName": "7d6fb03",
                        "HiveVersion": "2.1.1",
                        "KerberosInfo": {
                            "Krb5Conf": "config",
                            "KeyTab": "_t",
                            "ServicePrincipal": "3c1403"
                        },
                        "KerberosEnable": true
                    },
                    "Kafka": {
                        "InstanceId": "3c140219"
                    },
                    "OtherDatasourceConnection": {
                        "Location": {
                            "VpcId": "3c14b03",
                            "VpcCidrBlock": "d6fb03",
                            "SubnetId": "d8981h",
                            "SubnetCidrBlock": "s8u1d"
                        }
                    },
                    "PostgreSql": {
                        "InstanceId": "3c103",
                        "InstanceName": "0000154cb-10",
                        "JdbcUrl": "xxx.tencentcloudapi.com",
                        "User": "admin",
                        "Password": "user",
                        "DbName": "db1",
                        "Location": {
                            "VpcId": "vpc_h98f1",
                            "VpcCidrBlock": "vpc_851",
                            "SubnetId": "subnet_9hv48h7",
                            "SubnetCidrBlock": "block_129fu2"
                        }
                    },
                    "SqlServer": {
                        "InstanceId": "instance_v984r",
                        "InstanceName": "instance_v49n",
                        "JdbcUrl": "xxx.tencentcloudapi.com",
                        "User": "admin",
                        "Password": "password",
                        "DbName": "db1"
                    },
                    "ClickHouse": {
                        "InstanceId": "instance_vn491",
                        "InstanceName": "instacen_v49r",
                        "JdbcUrl": "xxx.tencentcloudapi.com",
                        "User": "user",
                        "Password": "password",
                        "DbName": "db1",
                        "Location": {
                            "VpcId": "vpc_v498n",
                            "VpcCidrBlock": "block_vj489",
                            "SubnetId": "subnet_c948",
                            "SubnetCidrBlock": "cidr_c39n"
                        }
                    },
                    "Elasticsearch": {
                        "InstanceId": "instance_c49n",
                        "InstanceName": "instance_m4c9",
                        "User": "user",
                        "Password": "password",
                        "DbName": "db1",
                        "Location": {
                            "VpcId": "vpc_12em0",
                            "VpcCidrBlock": "block_49n",
                            "SubnetId": "subnet_c4n9n",
                            "SubnetCidrBlock": "block_c49un"
                        },
                        "ServiceInfo": [
                            {
                                "Ip": "127.0.0.1",
                                "Port": 0
                            }
                        ]
                    },
                    "TCHouseD": {
                        "InstanceId": "instance_n59",
                        "InstanceName": "instance_v49",
                        "JdbcUrl": "xxx.tencentcloudapi.com",
                        "User": "admin",
                        "Password": "password",
                        "DbName": "db1",
                        "Location": {
                            "VpcId": "vpc_d92n",
                            "VpcCidrBlock": "cird_vm390",
                            "SubnetId": "subnet_1d09",
                            "SubnetCidrBlock": "block_v49j"
                        }
                    },
                    "TDSQLPostgreSql": {
                        "InstanceId": "instance_n59",
                        "InstanceName": "instance_v49",
                        "JdbcUrl": "xxx.tencentcloudapi.com",
                        "User": "admin",
                        "Password": "password",
                        "DbName": "db1",
                        "Location": {
                            "VpcId": "vpc_d92n",
                            "VpcCidrBlock": "cird_vm390",
                            "SubnetId": "subnet_1d09",
                            "SubnetCidrBlock": "block_v49j"
                        }
                    }
                },
                "State": 0,
                "Region": "shanghai",
                "AppId": "3jc9839n94n",
                "CreateTime": "2006-01-02 15:04:05",
                "UpdateTime": "2006-01-02 15:04:05",
                "Message": "success",
                "DataEngines": [
                    {
                        "DataEngineName": "engine_nuf1n9",
                        "QuotaId": "quota_1j918",
                        "EngineType": "normal",
                        "ClusterType": "cluster_1",
                        "State": 0,
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Size": 0,
                        "Mode": 0,
                        "MinClusters": 0,
                        "MaxClusters": 0,
                        "AutoResume": true,
                        "SpendAfter": 0,
                        "CidrBlock": "cidr_dm1oi",
                        "DefaultDataEngine": true,
                        "Message": "success",
                        "DataEngineId": "engine_1md1",
                        "SubAccountUin": "cj082j90n",
                        "ExpireTime": "2006-01-02 15:04:05",
                        "IsolatedTime": "2006-01-02 15:04:05",
                        "ReversalTime": "2006-01-02 15:04:05",
                        "UserAlias": "alis",
                        "TagList": [
                            {
                                "TagKey": "mfoi1ji",
                                "TagValue": "f1i00f"
                            }
                        ],
                        "Permissions": [
                            "suceess"
                        ],
                        "AutoSuspend": true,
                        "CrontabResumeSuspend": 0,
                        "CrontabResumeSuspendStrategy": {
                            "ResumeTime": "2006-01-02 15:04:05",
                            "SuspendTime": "2006-01-02 15:04:05",
                            "SuspendStrategy": 0
                        },
                        "EngineExecType": "tpye1",
                        "RenewFlag": 0,
                        "AutoSuspendTime": 0,
                        "NetworkConnectionSet": [
                            {
                                "Id": 0,
                                "AssociateId": "f01j",
                                "HouseId": "mv01n",
                                "DatasourceConnectionId": "connect_vn94n",
                                "State": 0,
                                "CreateTime": 0,
                                "UpdateTime": 0,
                                "Appid": 0,
                                "HouseName": "house_j9c82n",
                                "DatasourceConnectionName": "connection_1m9dn1",
                                "NetworkConnectionType": 0,
                                "Uin": "x9982jz",
                                "SubAccountUin": "m0cm9nxun20",
                                "NetworkConnectionDesc": "noraml",
                                "DatasourceConnectionVpcId": "vpc_19d8n1",
                                "DatasourceConnectionSubnetId": "subnet_c19n",
                                "DatasourceConnectionCidrBlock": "block_21j0",
                                "DatasourceConnectionSubnetCidrBlock": "cidr_1m2in"
                            }
                        ],
                        "UiURL": "xxx.tencentcloudapi.com",
                        "ResourceType": "normal",
                        "ImageVersionId": "2.1.1",
                        "ChildImageVersionId": "2.1.1",
                        "ImageVersionName": "2.1.1",
                        "StartStandbyCluster": true,
                        "ElasticSwitch": true,
                        "ElasticLimit": 0,
                        "DefaultHouse": true,
                        "MaxConcurrency": 0,
                        "TolerableQueueTime": 0,
                        "UserAppId": 0,
                        "UserUin": "vm0i2m",
                        "SessionResourceTemplate": {
                            "DriverSize": "200",
                            "ExecutorSize": "6",
                            "ExecutorNums": 1,
                            "ExecutorMaxNumbers": 1
                        },
                        "AutoAuthorization": true
                    }
                ],
                "UserAlias": "admin",
                "NetworkConnectionSet": [
                    {
                        "Id": 0,
                        "AssociateId": "4d7a-4f21",
                        "HouseId": "cfb78a9",
                        "DatasourceConnectionId": "7dbb774578a9",
                        "State": 0,
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Appid": 0,
                        "HouseName": "7cfb78a9",
                        "DatasourceConnectionName": "connnction",
                        "NetworkConnectionType": 0,
                        "Uin": "ecfb78a9",
                        "SubAccountUin": "78a9",
                        "NetworkConnectionDesc": "normal",
                        "DatasourceConnectionVpcId": "vpc_1md9",
                        "DatasourceConnectionSubnetId": "subnet_101n1",
                        "DatasourceConnectionCidrBlock": "block_vj9381",
                        "DatasourceConnectionSubnetCidrBlock": "cird_bn29n"
                    }
                ],
                "ConnectivityState": 1,
                "ConnectivityTips": "admin"
            }
        ],
        "RequestId": "7dbb7745-4d7a-4f21-b863-4971ecfb78a9"
    }
}
```

