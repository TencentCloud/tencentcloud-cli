**Example 1: 更新云数据库示例**



Input: 

```
tccli bi ModifyDatasourceCloud --cli-unfold-argument  \
    --Id 1 \
    --ProjectId abc \
    --SourceName 数据库别名 \
    --Vport 3306 \
    --VpcId 123456 \
    --Charset utf8 \
    --ExtraParam  \
    --DbUser root \
    --ServiceType {"Type":"Cloud","Region":"ap-guangzhou","InstanceId":"cdb-bdb0juh5"} \
    --DbType MySQL \
    --UniqVpcId vpc-123 \
    --RegionId gz \
    --DbName power-test \
    --DbPwd 12345 \
    --Vip 
```

Output: 
```
{
    "Response": {
        "RequestId": "63f50c98-1e5b-41bc-9a6a-d630312f8de9",
        "Extra": "",
        "Data": "",
        "Msg": "success"
    }
}
```

**Example 2: 更新云数据源**



Input: 

```
tccli bi ModifyDatasourceCloud --cli-unfold-argument  \
    --ServiceType abc \
    --DbType abc \
    --Charset abc \
    --DbUser abc \
    --DbPwd abc \
    --DbName abc \
    --SourceName abc \
    --ProjectId abc \
    --Vip abc \
    --Vport abc \
    --VpcId abc \
    --UniqVpcId abc \
    --RegionId abc \
    --ExtraParam abc \
    --Id 1 \
    --InstanceId abc \
    --ProdDbName abc
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "Extra": "abc",
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

