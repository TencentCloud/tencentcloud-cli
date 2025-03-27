**Example 1: 创建云数据库测示例**

创建云数据库测示例

Input: 

```
tccli bi CreateDatasourceCloud --cli-unfold-argument  \
    --ServiceType ServiceType \
    --DbType DbType \
    --Charset Charset \
    --DbUser DbUser \
    --DbPwd DbPwd \
    --DbName DbName \
    --SourceName SourceName \
    --ProjectId ProjectId \
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
        "Data": {
            "Id": 0,
            "AccessKey": "AccessKey***AccessKey",
            "ProjectId": 1,
            "TranId": "jgvk213439",
            "TranStatus": 0
        },
        "Extra": "",
        "Msg": "成功",
        "RequestId": "RequestId-123"
    }
}
```

