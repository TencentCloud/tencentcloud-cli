**Example 1: 示例一**

示例一

Input: 

```
tccli dlc AssignMangedTableProperties --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName dlc_db \
    --TableBaseInfo.TableName dlc_test \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.TableComment this is a test db \
    --TableBaseInfo.Type table \
    --TableBaseInfo.TableFormat iceberg \
    --TableBaseInfo.UserAlias xiaoming \
    --TableBaseInfo.SmartPolicy.BaseInfo.Uin 1000******03 \
    --TableBaseInfo.SmartPolicy.BaseInfo.PolicyType Table \
    --TableBaseInfo.SmartPolicy.BaseInfo.Catalog DataLakeCatalog \
    --TableBaseInfo.SmartPolicy.BaseInfo.Database dlc_db \
    --TableBaseInfo.SmartPolicy.BaseInfo.Table table_ai \
    --TableBaseInfo.SmartPolicy.BaseInfo.AppId 131****789 \
    --TableBaseInfo.SmartPolicy.Policy.Inherit none \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.AttributionType group \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.ResourceType SQL \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Name dlc_spark_test \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Instance spark-sql \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Priority 2147483647 \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Catalog DataLakeCatalog \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.DataBase dlc_db \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Table table_ai \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Status 1 \
    --TableBaseInfo.SmartPolicy.Policy.Written.WrittenEnable enable \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CompactEnable enable \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.DeleteEnable enable \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.MinInputFiles 5 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.TargetFileSizeBytes 134217728 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RetainLast 5 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.BeforeDays 2 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.ExpiredSnapshotsIntervalMin 600 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RemoveOrphanIntervalMin 1440 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CowCompactEnable disable \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CompactStrategy binpack \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.LifecycleEnable disable \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.Expiration 0 \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.DropTable True \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredField pt \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredFieldFormat yyyy-MM-dd \
    --TableBaseInfo.SmartPolicy.Policy.Index.IndexEnable disable \
    --Columns.0.Name name \
    --Columns.0.Type string \
    --Columns.0.Comment the age for user \
    --Columns.0.Default 0 \
    --Columns.0.NotNull True \
    --Columns.0.Precision 0 \
    --Columns.0.Scale 0 \
    --Partitions.0.Name name \
    --Partitions.0.Type string \
    --Partitions.0.Comment the age for user \
    --Properties.0.Key key1 \
    --Properties.0.Value value1 \
    --UpsertKeys 
```

Output: 
```
{
    "Response": {
        "Properties": [
            {
                "Key": "key1",
                "Value": "value1"
            },
            {
                "Key": "write.distribution-mode",
                "Value": "hash"
            },
            {
                "Key": "write.metadata.delete-after-commit.enabled",
                "Value": "true"
            },
            {
                "Key": "write.metadata.previous-versions-max",
                "Value": "100"
            },
            {
                "Key": "write.metadata.metrics.default",
                "Value": "full"
            },
            {
                "Key": "smart-optimizer.inherit",
                "Value": "none"
            },
            {
                "Key": "smart-optimizer.written.enable",
                "Value": "enable"
            },
            {
                "Key": "smart-optimizer.written.advance.compact-enable",
                "Value": "enable"
            },
            {
                "Key": "smart-optimizer.written.advance.cow-compact-enable",
                "Value": "disable"
            },
            {
                "Key": "smart-optimizer.written.advance.strategy",
                "Value": "binpack"
            },
            {
                "Key": "smart-optimizer.written.advance.sort-order",
                "Value": "nulls"
            },
            {
                "Key": "smart-optimizer.written.advance.min-input-files",
                "Value": "5"
            },
            {
                "Key": "smart-optimizer.written.advance.target-file-size-bytes",
                "Value": "134217728"
            },
            {
                "Key": "smart-optimizer.written.advance.delete-enable",
                "Value": "enable"
            },
            {
                "Key": "smart-optimizer.written.advance.retain-last",
                "Value": "5"
            },
            {
                "Key": "smart-optimizer.written.advance.before-days",
                "Value": "2"
            },
            {
                "Key": "smart-optimizer.written.advance.expired-snapshots-interval-min",
                "Value": "600"
            },
            {
                "Key": "smart-optimizer.written.advance.remove-orphan-interval-min",
                "Value": "1440"
            },
            {
                "Key": "smart-optimizer.lifecycle.enable",
                "Value": "disable"
            },
            {
                "Key": "lakehouse.storage.type",
                "Value": "lakefs"
            }
        ],
        "RequestId": "3f7509bf-20f9-4767-ab9c-0f9d901deda0"
    }
}
```

