**Example 1: 创建云数据库测示例**

创建云数据库测示例

Input: 

```
tccli bi CreateDatasourceCloud --cli-unfold-argument  \
    --ServiceType MYSQL \
    --DbType MYSQL \
    --Charset utf8 \
    --DbUser root \
    --DbPwd ****** \
    --DbName bi_demo \
    --SourceName  \
    --ProjectId  \
    --Vip  \
    --Vport  \
    --VpcId  \
    --UniqVpcId  \
    --RegionId 1 \
    --ExtraParam  \
    --InstanceId 1 \
    --ProdDbName 1 \
    --DataOrigin 1 \
    --DataOriginProjectId 1 \
    --DataOriginDatasourceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0,
            "AccessKey": "asakdsmsk**sdsmdsff",
            "ProjectId": 1,
            "TranId": "jgvk213439",
            "TranStatus": 0
        },
        "Extra": "",
        "Msg": "成功",
        "RequestId": "djdkssadlflksdkasjfrejq"
    }
}
```

