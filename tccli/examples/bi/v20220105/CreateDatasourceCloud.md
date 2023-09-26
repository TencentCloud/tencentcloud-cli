**Example 1: 创建云数据库测示例**

创建云数据库测示例

Input: 

```
tccli bi CreateDatasourceCloud --cli-unfold-argument  \
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
    --InstanceId abc \
    --ProdDbName abc \
    --DataOrigin abc \
    --DataOriginProjectId abc \
    --DataOriginDatasourceId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0,
            "AccessKey": "abc",
            "ProjectId": 1,
            "TranId": "abc",
            "TranStatus": 0
        },
        "Extra": "abc",
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

