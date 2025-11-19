**Example 1: 查询用户连接信息**

查询用户连接信息

Input: 

```
tccli dlc DescribeUserVpcConnection --cli-unfold-argument  \
    --EngineNetworkId DataEngine-Network-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ac4fff9d-b8a8-429c-88fb-c9cfaac1ec5a",
        "UserVpcConnectionInfos": [
            {
                "AccessConnectionInfos": [
                    "jdbc:hive2://10.0.0.14:10009/?kyuubi.engine.type=TRINO;kyuubi.session.engine.trino.connection.url=http://127.0.0.1:8080;kyuubi.session.engine.trino.connection.catalog=hive;kyuubi.operation.incremental.collect=true",
                    "jdbc:presto://10.0.0.14:10999/?sessionProperties=cluster:keyiliu_presto;region:{Region};database:{DatabaseName};catalog:hive&extraCredentials=secretkey:{SecretKey};secretid:{SecretId}"
                ],
                "UserVpcEndpointId": "vpce-7m3bgkj4",
                "UserVpcEndpointName": "rickytest",
                "UserVpcId": "vpc-dk19yfij"
            }
        ]
    }
}
```

