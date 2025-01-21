**Example 1: 创建托管存储内表**



Input: 

```
tccli dlc CreateInternalTable --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName devicedata_space \
    --TableBaseInfo.TableName test_ods \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.TableComment 测试用创建 \
    --TableBaseInfo.Type MANAGED_TABLE \
    --TableBaseInfo.TableFormat ICEBERG \
    --TableBaseInfo.UserAlias 1000xxxx663 \
    --TableBaseInfo.UserSubUin 1000xxxx663 \
    --Columns.0.Name id \
    --Columns.0.Type BIGINT \
    --Columns.0.Comment id \
    --Columns.0.Default 0 \
    --Columns.0.NotNull False \
    --Columns.0.Precision 0 \
    --Columns.0.Scale 0 \
    --Partitions.0.Name id \
    --Partitions.0.Type int \
    --Partitions.0.Comment id \
    --Partitions.0.PartitionDot 0 \
    --Partitions.0.Transform bucket \
    --Partitions.0.TransformArgs 16
```

Output: 
```
{
    "Response": {
        "Execution": "CREATE TABLE IF NOT EXISTS `DataLakeCatalog`.`data`.`test` (`id` BIGINT) COMMENT '测试用创建' TBLPROPERTIES ('write.distribution-mode'='hash', 'write.metadata.delete-after-commit.enabled'='true', 'write.metadata.previous-versions-max'='100', 'write.metadata.metrics.default'='full', 'smart-optimizer.inherit'='default');",
        "RequestId": "fdee5c95-4677-4ebe-b487-9aae77437426"
    }
}
```

