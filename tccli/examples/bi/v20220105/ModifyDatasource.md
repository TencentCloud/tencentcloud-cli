**Example 1: 更新数据源**



Input: 

```
tccli bi ModifyDatasource --cli-unfold-argument  \
    --DbHost 0.0.0.0 \
    --DbPort 3307 \
    --ServiceType {"Type":"Own"} \
    --DbType MONGODB \
    --DataOrigin  \
    --Charset utf8 \
    --Catalog  \
    --DbUser username \
    --DbName name \
    --DbPwd password \
    --SourceName 测试vpc \
    --VpcId vpcid \
    --UniqVpcId vpc- \
    --Vip  \
    --Vport  \
    --ExtraParam  \
    --DataOriginProjectId  \
    --DataOriginDatasourceId  \
    --UseVPC True \
    --RegionId gz \
    --ProjectId 517 \
    --Id 134
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

