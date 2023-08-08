**Example 1: 配置迁移任务**



Input: 

```
tccli dts ModifyMigrationJob --cli-unfold-argument  \
    --JobId abc \
    --JobName abc \
    --RunMode abc \
    --ExpectRunTime abc \
    --MigrateOption.MigrateType abc \
    --MigrateOption.Consistency.Mode abc \
    --MigrateOption.DatabaseTable.ObjectMode abc \
    --MigrateOption.DatabaseTable.Databases.0.DbName abc \
    --MigrateOption.DatabaseTable.Databases.0.NewDbName abc \
    --MigrateOption.DatabaseTable.Databases.0.SchemaName abc \
    --MigrateOption.DatabaseTable.Databases.0.NewSchemaName abc \
    --MigrateOption.DatabaseTable.Databases.0.DBMode abc \
    --MigrateOption.DatabaseTable.Databases.0.SchemaMode abc \
    --MigrateOption.DatabaseTable.Databases.0.TableMode abc \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableName abc \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.NewTableName abc \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TmpTables abc \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableEditMode abc \
    --MigrateOption.DatabaseTable.Databases.0.ViewMode abc \
    --MigrateOption.DatabaseTable.Databases.0.Views.0.ViewName abc \
    --MigrateOption.DatabaseTable.Databases.0.Views.0.NewViewName abc \
    --MigrateOption.DatabaseTable.Databases.0.RoleMode abc \
    --MigrateOption.DatabaseTable.Databases.0.Roles.0.RoleName abc \
    --MigrateOption.DatabaseTable.Databases.0.Roles.0.NewRoleName abc \
    --MigrateOption.DatabaseTable.Databases.0.FunctionMode abc \
    --MigrateOption.DatabaseTable.Databases.0.TriggerMode abc \
    --MigrateOption.DatabaseTable.Databases.0.EventMode abc \
    --MigrateOption.DatabaseTable.Databases.0.ProcedureMode abc \
    --MigrateOption.DatabaseTable.Databases.0.Functions abc \
    --MigrateOption.DatabaseTable.Databases.0.Procedures abc \
    --MigrateOption.DatabaseTable.Databases.0.Events abc \
    --MigrateOption.DatabaseTable.Databases.0.Triggers abc \
    --MigrateOption.DatabaseTable.AdvancedObjects abc \
    --MigrateOption.IsMigrateAccount True \
    --MigrateOption.IsOverrideRoot True \
    --MigrateOption.IsDstReadOnly True \
    --MigrateOption.ExtraAttr.0.Key abc \
    --MigrateOption.ExtraAttr.0.Value abc \
    --SrcInfo.Supplier abc \
    --SrcInfo.Region abc \
    --SrcInfo.AccessType abc \
    --SrcInfo.DatabaseType abc \
    --SrcInfo.NodeType abc \
    --SrcInfo.Info.0.Role abc \
    --SrcInfo.Info.0.DbKernel abc \
    --SrcInfo.Info.0.Host abc \
    --SrcInfo.Info.0.Port 1 \
    --SrcInfo.Info.0.User abc \
    --SrcInfo.Info.0.Password abc \
    --SrcInfo.Info.0.CvmInstanceId abc \
    --SrcInfo.Info.0.UniqVpnGwId abc \
    --SrcInfo.Info.0.UniqDcgId abc \
    --SrcInfo.Info.0.InstanceId abc \
    --SrcInfo.Info.0.CcnGwId abc \
    --SrcInfo.Info.0.VpcId abc \
    --SrcInfo.Info.0.SubnetId abc \
    --SrcInfo.Info.0.EngineVersion abc \
    --SrcInfo.Info.0.Account abc \
    --SrcInfo.Info.0.AccountRole abc \
    --SrcInfo.Info.0.AccountMode abc \
    --SrcInfo.Info.0.TmpSecretId abc \
    --SrcInfo.Info.0.TmpSecretKey abc \
    --SrcInfo.Info.0.TmpToken abc \
    --SrcInfo.ExtraAttr.0.Key abc \
    --SrcInfo.ExtraAttr.0.Value abc \
    --SrcInfo.DatabaseNetEnv abc \
    --DstInfo.Supplier abc \
    --DstInfo.Region abc \
    --DstInfo.AccessType abc \
    --DstInfo.DatabaseType abc \
    --DstInfo.NodeType abc \
    --DstInfo.Info.0.Role abc \
    --DstInfo.Info.0.DbKernel abc \
    --DstInfo.Info.0.Host abc \
    --DstInfo.Info.0.Port 1 \
    --DstInfo.Info.0.User abc \
    --DstInfo.Info.0.Password abc \
    --DstInfo.Info.0.CvmInstanceId abc \
    --DstInfo.Info.0.UniqVpnGwId abc \
    --DstInfo.Info.0.UniqDcgId abc \
    --DstInfo.Info.0.InstanceId abc \
    --DstInfo.Info.0.CcnGwId abc \
    --DstInfo.Info.0.VpcId abc \
    --DstInfo.Info.0.SubnetId abc \
    --DstInfo.Info.0.EngineVersion abc \
    --DstInfo.Info.0.Account abc \
    --DstInfo.Info.0.AccountRole abc \
    --DstInfo.Info.0.AccountMode abc \
    --DstInfo.Info.0.TmpSecretId abc \
    --DstInfo.Info.0.TmpSecretKey abc \
    --DstInfo.Info.0.TmpToken abc \
    --DstInfo.ExtraAttr.0.Key abc \
    --DstInfo.ExtraAttr.0.Value abc \
    --DstInfo.DatabaseNetEnv abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --AutoRetryTimeRangeMinutes 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

