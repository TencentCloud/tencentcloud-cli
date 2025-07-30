**Example 1: 更新数据源**



Input: 

```
tccli bi ModifyDatasource --cli-unfold-argument  \
    --DbHost DbHost \
    --DbPort 1982493789748932 \
    --ServiceType ServiceType \
    --DbType DbType \
    --Charset Charset \
    --DbUser DbUser \
    --DbPwd DbPwd \
    --DbName DbName \
    --SourceName SourceName \
    --Id 1982493789748932 \
    --ProjectId 1982493789748932 \
    --Catalog Catalog \
    --DataOrigin DataOrigin \
    --DataOriginProjectId DataOriginProjectId \
    --DataOriginDatasourceId DataOriginDatasourceId \
    --ExtraParam ExtraParam \
    --UniqVpcId UniqVpcId \
    --Vip Vip \
    --Vport Vport \
    --VpcId VpcId \
    --UseVPC False \
    --RegionId RegionId
```

Output: 
```
{
    "Response": {
        "Msg": "服务器内部错误",
        "RequestId": "xxx-xx-x",
        "Extra": "",
        "Data": null,
        "ErrorInfo": {
            "ErrorTip": "服务器内部错误",
            "ErrorMessage": "服务器内部错误",
            "ErrorLevel": "ERROR"
        }
    }
}
```

