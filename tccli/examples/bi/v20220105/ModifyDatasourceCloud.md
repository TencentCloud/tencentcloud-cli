**Example 1: 更新云数据库示例**



Input: 

```
tccli bi ModifyDatasourceCloud --cli-unfold-argument  \
    --Id 1 \
    --ProjectId 21313 \
    --SourceName 数据库别名 \
    --Vport 3306 \
    --VpcId 2131314 \
    --Charset utf8 \
    --ExtraParam  \
    --DbUser root \
    --ServiceType {"Type":"Cloud","Region":"ap-guangzhou","InstanceId":"cdb-bdb0juh5"} \
    --DbType MySQL \
    --UniqVpcId vpc-54343 \
    --RegionId gz \
    --DbName power-test \
    --DbPwd 2424***231312 \
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

