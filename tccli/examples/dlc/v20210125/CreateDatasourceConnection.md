**Example 1: 创建mysql数据源**

创建mysql数据源

Input: 

```
tccli dlc CreateDatasourceConnection --cli-unfold-argument  \
    --DatasourceConnectionName test \
    --DatasourceConnectionType Mysql \
    --DatasourceConnectionConfig.Mysql.JdbcUrl jdbc:mysql://ip:port \
    --DatasourceConnectionConfig.Mysql.User root \
    --DatasourceConnectionConfig.Mysql.Password awfwegew \
    --ServiceType DLC \
    --DatasourceConnectionDesc datasource test \
    --NetworkConnectionName test \
    --NetworkConnectionDesc test \
    --NetworkConnectionType 2
```

Output: 
```
{
    "Response": {
        "DatasourceConnectionId": "datasource-xxx",
        "RequestId": "e9fbdc29-93e1-40a1-afe1-871bf73ff92b"
    }
}
```

