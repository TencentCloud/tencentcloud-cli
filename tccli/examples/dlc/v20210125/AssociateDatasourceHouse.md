**Example 1: test**



Input: 

```
tccli dlc AssociateDatasourceHouse --cli-unfold-argument  \
    --DatasourceConnectionName abc \
    --DatasourceConnectionType abc \
    --DatasourceConnectionConfig.Mysql.JdbcUrl abc \
    --DatasourceConnectionConfig.Mysql.User abc \
    --DatasourceConnectionConfig.Mysql.Password abc \
    --DatasourceConnectionConfig.Mysql.Location.VpcId abc \
    --DatasourceConnectionConfig.Mysql.Location.VpcCidrBlock abc \
    --DatasourceConnectionConfig.Mysql.Location.SubnetId abc \
    --DatasourceConnectionConfig.Mysql.Location.SubnetCidrBlock abc \
    --DatasourceConnectionConfig.Mysql.DbName abc \
    --DatasourceConnectionConfig.Mysql.InstanceId abc \
    --DatasourceConnectionConfig.Mysql.InstanceName abc \
    --DatasourceConnectionConfig.Hive.MetaStoreUrl abc \
    --DatasourceConnectionConfig.Hive.Type abc \
    --DatasourceConnectionConfig.Hive.User abc \
    --DatasourceConnectionConfig.Hive.HighAvailability True \
    --DatasourceConnectionConfig.Hive.BucketUrl abc \
    --DatasourceConnectionConfig.Hive.HdfsProperties abc \
    --DatasourceConnectionConfig.Hive.Location.VpcId abc \
    --DatasourceConnectionConfig.Hive.Location.VpcCidrBlock abc \
    --DatasourceConnectionConfig.Hive.Location.SubnetId abc \
    --DatasourceConnectionConfig.Hive.Location.SubnetCidrBlock abc \
    --DatasourceConnectionConfig.Hive.Mysql.JdbcUrl abc \
    --DatasourceConnectionConfig.Hive.Mysql.User abc \
    --DatasourceConnectionConfig.Hive.Mysql.Password abc \
    --DatasourceConnectionConfig.Hive.Mysql.Location.VpcId abc \
    --DatasourceConnectionConfig.Hive.Mysql.Location.VpcCidrBlock abc \
    --DatasourceConnectionConfig.Hive.Mysql.Location.SubnetId abc \
    --DatasourceConnectionConfig.Hive.Mysql.Location.SubnetCidrBlock abc \
    --DatasourceConnectionConfig.Hive.Mysql.DbName abc \
    --DatasourceConnectionConfig.Hive.Mysql.InstanceId abc \
    --DatasourceConnectionConfig.Hive.Mysql.InstanceName abc \
    --DatasourceConnectionConfig.Hive.InstanceId abc \
    --DatasourceConnectionConfig.Hive.InstanceName abc \
    --DatasourceConnectionConfig.Hive.HiveVersion abc \
    --DatasourceConnectionConfig.Hive.KerberosInfo.Krb5Conf abc \
    --DatasourceConnectionConfig.Hive.KerberosInfo.KeyTab abc \
    --DatasourceConnectionConfig.Hive.KerberosInfo.ServicePrincipal abc \
    --DatasourceConnectionConfig.Hive.KerberosEnable True \
    --DatasourceConnectionConfig.Kafka.InstanceId abc \
    --DatasourceConnectionConfig.OtherDatasourceConnection.Location.VpcId abc \
    --DatasourceConnectionConfig.OtherDatasourceConnection.Location.VpcCidrBlock abc \
    --DatasourceConnectionConfig.OtherDatasourceConnection.Location.SubnetId abc \
    --DatasourceConnectionConfig.OtherDatasourceConnection.Location.SubnetCidrBlock abc \
    --DatasourceConnectionConfig.PostgreSql.InstanceId abc \
    --DatasourceConnectionConfig.PostgreSql.InstanceName abc \
    --DatasourceConnectionConfig.PostgreSql.JdbcUrl abc \
    --DatasourceConnectionConfig.PostgreSql.User abc \
    --DatasourceConnectionConfig.PostgreSql.Password abc \
    --DatasourceConnectionConfig.PostgreSql.DbName abc \
    --DatasourceConnectionConfig.SqlServer.InstanceId abc \
    --DatasourceConnectionConfig.SqlServer.InstanceName abc \
    --DatasourceConnectionConfig.SqlServer.JdbcUrl abc \
    --DatasourceConnectionConfig.SqlServer.User abc \
    --DatasourceConnectionConfig.SqlServer.Password abc \
    --DatasourceConnectionConfig.SqlServer.DbName abc \
    --DatasourceConnectionConfig.ClickHouse.InstanceId abc \
    --DatasourceConnectionConfig.ClickHouse.InstanceName abc \
    --DatasourceConnectionConfig.ClickHouse.JdbcUrl abc \
    --DatasourceConnectionConfig.ClickHouse.User abc \
    --DatasourceConnectionConfig.ClickHouse.Password abc \
    --DatasourceConnectionConfig.ClickHouse.DbName abc \
    --DatasourceConnectionConfig.Elasticsearch.InstanceId abc \
    --DatasourceConnectionConfig.Elasticsearch.InstanceName abc \
    --DatasourceConnectionConfig.Elasticsearch.User abc \
    --DatasourceConnectionConfig.Elasticsearch.Password abc \
    --DatasourceConnectionConfig.Elasticsearch.DbName abc \
    --DatasourceConnectionConfig.Elasticsearch.ServiceInfo.0.Ip abc \
    --DatasourceConnectionConfig.Elasticsearch.ServiceInfo.0.Port 0 \
    --DataEngineNames abc \
    --NetworkConnectionType 0 \
    --NetworkConnectionDesc abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

