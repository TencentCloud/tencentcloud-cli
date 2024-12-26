**Example 1: 配置迁移任务**



Input: 

```
tccli dts ModifyMigrationJob --cli-unfold-argument  \
    --JobId dts-efyc7e7l \
    --JobName dts-efyc7e7l \
    --RunMode immediate \
    --ExpectRunTime 2024-12-20 19:01:07 \
    --MigrateOption.MigrateType fullAndIncrement \
    --MigrateOption.Consistency.Mode full \
    --MigrateOption.DatabaseTable.ObjectMode partial \
    --MigrateOption.DatabaseTable.Databases.0.DbName db_1 \
    --MigrateOption.DatabaseTable.Databases.0.NewDbName  \
    --MigrateOption.DatabaseTable.Databases.0.SchemaName  \
    --MigrateOption.DatabaseTable.Databases.0.NewSchemaName  \
    --MigrateOption.DatabaseTable.Databases.0.DBMode partial \
    --MigrateOption.DatabaseTable.Databases.0.SchemaMode  \
    --MigrateOption.DatabaseTable.Databases.0.TableMode partial \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableName tb_1 \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.NewTableName  \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableEditMode  \
    --MigrateOption.DatabaseTable.Databases.0.ViewMode partial \
    --MigrateOption.DatabaseTable.Databases.0.Views.0.ViewName view_tb_1 \
    --MigrateOption.DatabaseTable.Databases.0.Views.0.NewViewName  \
    --MigrateOption.DatabaseTable.Databases.0.RoleMode  \
    --MigrateOption.DatabaseTable.Databases.0.FunctionMode  \
    --MigrateOption.DatabaseTable.Databases.0.TriggerMode  \
    --MigrateOption.DatabaseTable.Databases.0.EventMode  \
    --MigrateOption.DatabaseTable.Databases.0.ProcedureMode  \
    --MigrateOption.IsMigrateAccount True \
    --MigrateOption.IsOverrideRoot True \
    --MigrateOption.IsDstReadOnly True \
    --SrcInfo.Supplier  \
    --SrcInfo.Region ap-qingyuan \
    --SrcInfo.AccessType cdb \
    --SrcInfo.DatabaseType mysql \
    --SrcInfo.NodeType  \
    --SrcInfo.Info.0.Role  \
    --SrcInfo.Info.0.DbKernel  \
    --SrcInfo.Info.0.Host  \
    --SrcInfo.Info.0.Port 0 \
    --SrcInfo.Info.0.User tencent \
    --SrcInfo.Info.0.Password tencent*** \
    --SrcInfo.Info.0.CvmInstanceId  \
    --SrcInfo.Info.0.UniqVpnGwId  \
    --SrcInfo.Info.0.UniqDcgId  \
    --SrcInfo.Info.0.InstanceId cdb-4gp2nzqy \
    --SrcInfo.Info.0.CcnGwId  \
    --SrcInfo.Info.0.VpcId  \
    --SrcInfo.Info.0.SubnetId  \
    --SrcInfo.Info.0.EngineVersion 8.0 \
    --SrcInfo.Info.0.Account  \
    --SrcInfo.Info.0.AccountRole  \
    --SrcInfo.Info.0.AccountMode  \
    --SrcInfo.Info.0.TmpSecretId  \
    --SrcInfo.Info.0.TmpSecretKey  \
    --SrcInfo.Info.0.TmpToken  \
    --SrcInfo.DatabaseNetEnv  \
    --DstInfo.Supplier  \
    --DstInfo.Region ap-qingyuan \
    --DstInfo.AccessType cdb \
    --DstInfo.DatabaseType mysql \
    --DstInfo.NodeType  \
    --DstInfo.Info.0.Role  \
    --DstInfo.Info.0.DbKernel  \
    --DstInfo.Info.0.Host  \
    --DstInfo.Info.0.Port 0 \
    --DstInfo.Info.0.User tencent \
    --DstInfo.Info.0.Password tencent*** \
    --DstInfo.Info.0.CvmInstanceId  \
    --DstInfo.Info.0.UniqVpnGwId  \
    --DstInfo.Info.0.UniqDcgId  \
    --DstInfo.Info.0.InstanceId cdb-4gp2nzqy \
    --DstInfo.Info.0.CcnGwId  \
    --DstInfo.Info.0.VpcId  \
    --DstInfo.Info.0.SubnetId  \
    --DstInfo.Info.0.EngineVersion 8.0 \
    --DstInfo.Info.0.Account  \
    --DstInfo.Info.0.AccountRole  \
    --DstInfo.Info.0.AccountMode  \
    --DstInfo.Info.0.TmpSecretId  \
    --DstInfo.Info.0.TmpSecretKey  \
    --DstInfo.Info.0.TmpToken  \
    --DstInfo.DatabaseNetEnv  \
    --AutoRetryTimeRangeMinutes 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a3365b29-2042-4565-9206-8df9e2af1a17"
    }
}
```

