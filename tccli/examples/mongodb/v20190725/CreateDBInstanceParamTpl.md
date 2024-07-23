**Example 1: 创建参数模板**



Input: 

```
tccli mongodb CreateDBInstanceParamTpl --cli-unfold-argument  \
    --ClusterType SHARD \
    --MongoVersion MONGO_44_WT \
    --TplDesc  \
    --TplName test-4.4
```

Output: 
```
{
    "Response": {
        "RequestId": "f3924f2d-6b76-4fe3-b705-1e0144049b90",
        "TplId": "tpl-bi5f78srm"
    }
}
```

