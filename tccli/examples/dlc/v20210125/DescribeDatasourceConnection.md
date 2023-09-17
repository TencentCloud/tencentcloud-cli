**Example 1: 查询数据源信息**



Input: 

```
tccli dlc DescribeDatasourceConnection --cli-unfold-argument  \
    --Sorting desc \
    --DatasourceConnectionIds 10001 10002 \
    --Limit 20 \
    --SortBy create_time \
    --Filters.0.Values DataLakeCatalog \
    --Filters.0.Name DatasourceConnectionName \
    --Offset 0 \
    --StartTime 2022-01-02 15:04:05 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ConnectionSet": [
            {
                "DatasourceConnectionConfig": {
                    "Hive": {
                        "Type": "COS",
                        "MetaStoreUrl": "thrift://127.0.0.1:9083",
                        "HdfsProperties": "fs.defaultFS=hdfs://ip:port",
                        "User": "hadoop",
                        "HighAvailability": false,
                        "Mysql": {
                            "Location": {
                                "SubnetId": "subnet-bthucmmy",
                                "VpcId": "vpc-azd4dt1c",
                                "VpcCidrBlock": "10.0.0.0/24",
                                "SubnetCidrBlock": "10.0.0.0/24"
                            },
                            "Password": "****",
                            "DbName": "MetaDb",
                            "User": "root",
                            "JdbcUrl": "jdbc:mysql://ip:port"
                        },
                        "BucketUrl": "cosn://bucketname/path",
                        "Location": {
                            "SubnetId": "subnet-bthucmmy",
                            "VpcId": "vpc-azd4dt1c",
                            "VpcCidrBlock": "10.0.0.0/24",
                            "SubnetCidrBlock": "10.0.0.0/24"
                        }
                    },
                    "Mysql": {
                        "Location": {
                            "SubnetId": "subnet-bthucmmy",
                            "VpcId": "vpc-azd4dt1c",
                            "VpcCidrBlock": "10.0.0.0/24",
                            "SubnetCidrBlock": "10.0.0.0/24"
                        },
                        "Password": "****",
                        "DbName": "MetaDb",
                        "User": "root",
                        "JdbcUrl": "jdbc:mysql://ip:port"
                    }
                },
                "DatasourceConnectionName": "DataLakeCatalog",
                "DatasourceConnectionId": "datasource-nvxud35v",
                "UpdateTime": "2021-01-01 00:00:00",
                "CreateTime": "2021-01-01 00:00:00",
                "State": 0,
                "Region": "ap-beijjing",
                "AppId": "123***789",
                "Message": "success",
                "DatasourceConnectionType": "DataLakeCatalog",
                "DatasourceConnectionDesc": "测试数据源",
                "Id": 0
            }
        ],
        "RequestId": "b577857e-041f-46c7-b5cf-4b3d3f50bc51"
    }
}
```

