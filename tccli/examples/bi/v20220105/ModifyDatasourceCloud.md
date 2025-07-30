**Example 1: 更新云数据库示例**



Input: 

```
tccli bi ModifyDatasourceCloud --cli-unfold-argument  \
    --ServiceType ServiceType \
    --DbType DbType \
    --Charset Charset \
    --DbUser DbUser \
    --DbPwd DbPwd \
    --DbName DbName \
    --SourceName SourceName \
    --ProjectId ProjectId \
    --Id 1982493789748932 \
    --Vip Vip \
    --Vport Vport \
    --VpcId VpcId \
    --UniqVpcId UniqVpcId \
    --RegionId RegionId \
    --ExtraParam ExtraParam \
    --InstanceId InstanceId \
    --ProdDbName ProdDbName \
    --DataOrigin DataOrigin \
    --DataOriginProjectId DataOriginProjectId \
    --DataOriginDatasourceId DataOriginDatasourceId \
    --ClusterId ClusterId
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

