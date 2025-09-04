**Example 1: 创建tc-iceberg表**

创建tc-iceberg表

Input: 

```
tccli dlc CreateTcIcebergTable --cli-unfold-argument  \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.DatabaseName yuxinghe_test_0212 \
    --TableBaseInfo.TableName demo_tb \
    --TableBaseInfo.SmartPolicy.BaseInfo.Uin 100018379117 \
    --TableBaseInfo.SmartPolicy.BaseInfo.AppId 1305424723 \
    --TableBaseInfo.SmartPolicy.BaseInfo.PolicyType Table \
    --TableBaseInfo.SmartPolicy.BaseInfo.Catalog DataLakeCatalog \
    --TableBaseInfo.SmartPolicy.BaseInfo.Database yuxinghe_test_0212 \
    --TableBaseInfo.SmartPolicy.BaseInfo.Table demo_tb \
    --TableBaseInfo.SmartPolicy.Policy.Inherit none \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Name 277-spark35-test-yuxinghe \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.ResourceType SQL \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.AttributionType group \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.ResourceGroupName test-277-group \
    --TableBaseInfo.SmartPolicy.Policy.Written.WrittenEnable enable \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.LifecycleEnable enable \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.Expiration 30 \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredFieldFormat yyyy-MM-dd \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredField col1 \
    --TableBaseInfo.SmartPolicy.Policy.Index.IndexEnable disable \
    --TableBaseInfo.SmartPolicy.Policy.ChangeTable.DataRetentionTime 7 \
    --TableBaseInfo.PrimaryKeys col1 \
    --TableBaseInfo.TableFormat TC-ICEBERG \
    --Columns.0.Name col1 \
    --Columns.0.Type string \
    --Columns.1.Name col2 \
    --Columns.1.Type int \
    --Partitions.0.Name col1 \
    --Partitions.0.Transform identity \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "DryRun": false,
        "RequestId": "deb07535-ccd2-4574-846b-d675249a7f47",
        "SQL": "CREATE TABLE IF NOT EXISTS yuxinghe_test_0212.demo_tb ( col1 string, col2 int, primary key(col1)) USING MIXED_ICEBERG PARTITIONED BY (col1) TBLPROPERTIES ('change.data.ttl.minutes'='10080', 'clean-dangling-delete-files.enabled'='true', 'clean-orhan-files.interval'='1440', 'clean-orphan-file.enabled'='true', 'data-expire.datetime-string-pattern'='yyyy-MM-dd', 'data-expire.enabled'='true', 'data-expire.field'='col1', 'data-expire.retention-time'='30d', 'dlc_sub_uin'='100018379117', 'lakehouse.storage.type'='lakefs', 'optimizing.engine.name'='277-spark35-test-yuxinghe', 'optimizing.engine.resource.group.name'='test-277-group', 'self-optimizing.enabled'='true', 'self-optimizing.group'='dlc_1305424723_277-spark35-test-yux_opti_grp', 'self-optimizing.minor.trigger.file-count'='5', 'self-optimizing.target-size'='134217728', 'smart-optimizer.inherit'='none', 'snapshot-expire.interval'='600', 'snapshot.base.keep.count'='5', 'snapshot.base.keep.minutes'='2880', 'table-expire.enabled'='true', 'write.distribution-mode'='hash', 'write.metadata.delete-after-commit.enabled'='true', 'write.metadata.previous-versions-max'='100', 'write.metadata.metrics.default'='full');",
        "SessionId": "09b4d457-c0f7-45c7-bc0e-46398322f0dc-SIMPLE-1305424723:DataLakeCatalog:zYBEmJFg:u7CzujF-DataLakeCatalog"
    }
}
```

