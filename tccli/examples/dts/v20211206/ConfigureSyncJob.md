**Example 1: 配置同步任务**

配置一个同步整库的同步任务

Input: 

```
tccli dts ConfigureSyncJob --cli-unfold-argument  \
    --DstInfo.Ip 9.123.210.46 \
    --DstInfo.Password Test1234 \
    --DstInfo.User root \
    --DstInfo.Port 30654 \
    --SrcInfo.Ip 9.123.211.23 \
    --SrcInfo.Password Test1234 \
    --SrcInfo.User root \
    --SrcInfo.Port 30645 \
    --ExpectRunTime 0000-00-00 00:00:01 \
    --DstAccessType noProxy \
    --JobName truexu-api \
    --RunMode Immediate \
    --Objects.Mode Partial \
    --Objects.Databases.0.DbName db1 \
    --Objects.Databases.0.DbMode All \
    --Objects.Databases.0.TableMode All \
    --Objects.Databases.0.Tables None \
    --Objects.Databases.0.ViewMode All \
    --Objects.Databases.0.Views None \
    --Objects.Databases.0.FunctionMode All \
    --Objects.Databases.0.TriggerMode  \
    --Objects.Databases.0.EventMode  \
    --Objects.Databases.0.ProcedureMode All \
    --Objects.Databases.0.Functions None \
    --Objects.Databases.0.Procedures None \
    --Objects.Databases.0.Events None \
    --Objects.Databases.0.Triggers None \
    --JobId sync-7r1cz016 \
    --Options.DealOfExistSameTable ExecuteAfterIgnore \
    --Options.OpTypes Update \
    --Options.DdlOptions.0.DdlObject Database \
    --Options.DdlOptions.0.DdlValue Create Alter \
    --Options.InitType Full \
    --Options.ConflictHandleOption.ConditionColumn ts \
    --Options.ConflictHandleOption.ConditionOperator > \
    --Options.ConflictHandleOption.ConditionOrderInSrcAndDst < \
    --SrcAccessType noProxy
```

Output: 
```
{
    "Response": {
        "RequestId": "8d495a08-5f8f-411b-ae4d-cc6da2475b9c"
    }
}
```

**Example 2: 配置同步任务2**

配置一个同步包含条件覆盖的任务

Input: 

```
tccli dts ConfigureSyncJob --cli-unfold-argument  \
    --DstInfo.Ip 100.88.178.199 \
    --DstInfo.Password Test1234 \
    --DstInfo.User root \
    --DstInfo.Port 20152 \
    --SrcInfo.Ip 100.88.166.23 \
    --SrcInfo.Password Test1234 \
    --SrcInfo.User root \
    --SrcInfo.Port 20126 \
    --ExpectRunTime 2021-12-08 11:59:05 \
    --DstAccessType noProxy \
    --JobName truex \
    --RunMode Immediate \
    --Objects.Mode Partial \
    --Objects.Databases.0.Tables.0.FilterCondition id>1 \
    --Objects.Databases.0.Tables.0.TableName tb1 \
    --Objects.Databases.0.Tables.0.NewTableName tb2 \
    --Objects.Databases.0.Views.0.ViewName vw1 \
    --Objects.Databases.0.Views.0.NewViewName vw2 \
    --Objects.Databases.0.DbName db1 \
    --Objects.Databases.0.ViewMode Partial \
    --Objects.Databases.0.TableMode Partial \
    --Objects.Databases.0.DbMode Partial \
    --JobId sync-31t047r6 \
    --Options.DdlOptions.0.DdlObject Database \
    --Options.DdlOptions.0.DdlValue Drop \
    --Options.ConflictHandleType ReportError \
    --Options.DealOfExistSameTable ReportErrorAfterCheck \
    --Options.ConflictHandleOption.ConditionColumn ts \
    --Options.ConflictHandleOption.ConditionOperator > \
    --Options.ConflictHandleOption.ConditionOrderInSrcAndDst > \
    --Options.InitType Full \
    --Options.OpTypes Insert Update \
    --Options.AddAdditionalColumn false \
    --SrcAccessType noProxy
```

Output: 
```
{
    "Response": {
        "RequestId": "59dd9972-00e7-4ce3-8f33-72d13bc64400"
    }
}
```

