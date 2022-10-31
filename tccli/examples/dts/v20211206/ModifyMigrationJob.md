**Example 1: 配置迁移服务**



Input: 

```
tccli dts ModifyMigrationJob --cli-unfold-argument  \
    --JobId dts-amm1jw5q \
    --JobName test_config_api \
    --RunMode immediate \
    --ExpectRunTime  \
    --MigrateOption.MigrateType fullAndIncrement \
    --MigrateOption.Consistency.Mode full \
    --MigrateOption.DatabaseTable.ObjectMode partial \
    --MigrateOption.DatabaseTable.Databases.0.DbName big100 \
    --MigrateOption.DatabaseTable.Databases.0.NewDbName  \
    --MigrateOption.DatabaseTable.Databases.0.SchemaName  \
    --MigrateOption.DatabaseTable.Databases.0.NewSchemaName  \
    --MigrateOption.DatabaseTable.Databases.0.DBMode partial \
    --MigrateOption.DatabaseTable.Databases.0.SchemaMode  \
    --MigrateOption.DatabaseTable.Databases.0.TableMode partial \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.NewTableName  \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableEditMode  \
    --MigrateOption.DatabaseTable.Databases.0.Tables.0.TableName sbtest1 \
    --MigrateOption.DatabaseTable.Databases.0.Tables.1.NewTableName new_sbtest10 \
    --MigrateOption.DatabaseTable.Databases.0.Tables.1.TableEditMode rename \
    --MigrateOption.DatabaseTable.Databases.0.Tables.1.TableName sbtest10 \
    --MigrateOption.DatabaseTable.Databases.0.Tables.2.NewTableName  \
    --MigrateOption.DatabaseTable.Databases.0.Tables.2.TableEditMode  \
    --MigrateOption.DatabaseTable.Databases.0.Tables.2.TableName sbtest100 \
    --MigrateOption.DatabaseTable.Databases.0.ViewMode partial \
    --MigrateOption.DatabaseTable.Databases.1.DbName db1 \
    --MigrateOption.DatabaseTable.Databases.1.DBMode all \
    --MigrateOption.IsMigrateAccount False \
    --SrcInfo.AccessType intranet \
    --SrcInfo.DatabaseType mysql \
    --SrcInfo.Info.0.Account  \
    --SrcInfo.Info.0.AccountMode  \
    --SrcInfo.Info.0.AccountRole  \
    --SrcInfo.Info.0.CcnGwId  \
    --SrcInfo.Info.0.CvmInstanceId  \
    --SrcInfo.Info.0.DbKernel  \
    --SrcInfo.Info.0.EngineVersion  \
    --SrcInfo.Info.0.Host 9.123.456.789 \
    --SrcInfo.Info.0.InstanceId  \
    --SrcInfo.Info.0.Password xxx \
    --SrcInfo.Info.0.Port 31035 \
    --SrcInfo.Info.0.Role  \
    --SrcInfo.Info.0.SubnetId  \
    --SrcInfo.Info.0.TmpSecretId  \
    --SrcInfo.Info.0.TmpSecretKey  \
    --SrcInfo.Info.0.TmpToken  \
    --SrcInfo.Info.0.UniqDcgId  \
    --SrcInfo.Info.0.UniqVpnGwId  \
    --SrcInfo.Info.0.User root \
    --SrcInfo.Info.0.VpcId  \
    --SrcInfo.NodeType simple \
    --SrcInfo.Region ap-guangzhou \
    --SrcInfo.Supplier  \
    --DstInfo.AccessType cdb \
    --DstInfo.DatabaseType mysql \
    --DstInfo.Info.0.Account  \
    --DstInfo.Info.0.AccountMode  \
    --DstInfo.Info.0.AccountRole  \
    --DstInfo.Info.0.CcnGwId  \
    --DstInfo.Info.0.CvmInstanceId  \
    --DstInfo.Info.0.DbKernel  \
    --DstInfo.Info.0.EngineVersion  \
    --DstInfo.Info.0.Host  \
    --DstInfo.Info.0.InstanceId cdb-o7uph0cj \
    --DstInfo.Info.0.Password xxx \
    --DstInfo.Info.0.Port 0 \
    --DstInfo.Info.0.Role  \
    --DstInfo.Info.0.SubnetId  \
    --DstInfo.Info.0.TmpSecretId  \
    --DstInfo.Info.0.TmpSecretKey  \
    --DstInfo.Info.0.TmpToken  \
    --DstInfo.Info.0.UniqDcgId  \
    --DstInfo.Info.0.UniqVpnGwId  \
    --DstInfo.Info.0.User root \
    --DstInfo.Info.0.VpcId  \
    --DstInfo.NodeType  \
    --DstInfo.Region ap-guangzhou \
    --DstInfo.Supplier  \
    --Tags.0.TagKey tag2 \
    --Tags.0.TagValue tag2
```

Output: 
```
{
    "Response": {
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

