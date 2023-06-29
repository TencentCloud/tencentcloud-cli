**Example 1: 配置修改对象任务**

在需要修改对象时、通过该接口开始配置修改对象的任务

Input: 

```
tccli dts ModifySyncJobConfig --cli-unfold-argument  \
    --JobId sync-4t8k7e8t \
    --DynamicObjects.Mode Partial \
    --DynamicObjects.Databases.0.DbName db1 \
    --DynamicObjects.Databases.0.DbMode All \
    --DynamicObjects.Databases.0.TableMode All \
    --DynamicObjects.Databases.0.ViewMode All \
    --DynamicOptions.ConflictHandleType ReportError \
    --DynamicOptions.DdlOptions.0.DdlObject Database \
    --DynamicOptions.DdlOptions.1.DdlObject Table \
    --DynamicOptions.DdlOptions.2.DdlObject View \
    --DynamicOptions.DdlOptions.3.DdlObject Index \
    --DynamicOptions.OpTypes Insert Update Delete DDL
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxaasassas"
    }
}
```

