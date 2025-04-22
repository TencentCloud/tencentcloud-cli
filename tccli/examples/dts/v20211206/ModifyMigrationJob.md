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
    --SrcInfo.Info.0.EncryptConn Encrypted \
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
    --DstInfo.Info.0.EncryptConn Encrypted \
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

**Example 2: 配置一个直连下云的redis迁移任务**

1.源端为腾讯云redis实例，目标端为AWS实例并以公网的方式连接目标节点信息填写所有分片上的IP/域名、端口、密码等连接信息；注意一定是所有分片节点连接信息都写。
2.目标端以覆盖写的方式执行，如果要配置其他目标端写入模式，可以参考入参MigrateOption.ExtraAttr中的字段描述。

Input: 

```
tccli dts ModifyMigrationJob --cli-unfold-argument  \
    --JobId dts-n6uzsuxz \
    --RunMode immediate \
    --MigrateOption.DatabaseTable.ObjectMode all \
    --MigrateOption.MigrateType fullAndIncrement \
    --MigrateOption.ExtraAttr.0.Key DstWriteMode \
    --MigrateOption.ExtraAttr.0.Value overwrite \
    --SrcInfo.Region ap-chengdu \
    --SrcInfo.AccessType cdb \
    --SrcInfo.DatabaseType redis \
    --SrcInfo.NodeType simple \
    --SrcInfo.Info.0.Password admin12345 \
    --SrcInfo.Info.0.InstanceId crs-lktt4ls3 \
    --DstInfo.Region ap-chengdu \
    --DstInfo.AccessType extranet \
    --DstInfo.DatabaseType redis \
    --DstInfo.NodeType cluster-cache \
    --DstInfo.Info.0.Host 44.223.107.125 \
    --DstInfo.Info.0.Port 6383 \
    --DstInfo.Info.1.Host 44.223.107.125 \
    --DstInfo.Info.1.Port 6384 \
    --DstInfo.Info.2.Host 44.223.107.125 \
    --DstInfo.Info.2.Port 6385
```

Output: 
```
{
    "Response": {
        "RequestId": "4d21a953-4a23-47f1-91a9-84df62f016f3"
    }
}
```

