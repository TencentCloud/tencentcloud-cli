**Example 1: 创建数据源**

创建数据源

Input: 

```
tccli bi CreateDatasource --cli-unfold-argument  \
    --DbHost abc \
    --DbPort 1 \
    --ServiceType abc \
    --DbType abc \
    --Charset abc \
    --DbUser abc \
    --DbPwd abc \
    --DbName abc \
    --SourceName abc \
    --ProjectId 1 \
    --Catalog abc \
    --DataOrigin abc \
    --DataOriginProjectId abc \
    --DataOriginDatasourceId abc \
    --ExtraParam abc \
    --UniqVpcId abc \
    --Vip abc \
    --Vport abc \
    --VpcId abc
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

