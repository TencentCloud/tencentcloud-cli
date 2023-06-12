**Example 1: 创建托管存储内表**

创建托管存储内表

Input: 

```
tccli dlc GenerateCreateMangedTableSql --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName abc \
    --TableBaseInfo.TableName abc \
    --TableBaseInfo.DatasourceConnectionName abc \
    --TableBaseInfo.TableComment abc \
    --TableBaseInfo.Type abc \
    --TableBaseInfo.TableFormat abc \
    --TableBaseInfo.UserAlias abc \
    --TableBaseInfo.UserSubUin abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.RewriteDataEnable abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.MinInputFiles 0 \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.TargetFileSizeBytes 0 \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.ExpiredSnapshotsEnable abc \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.RetainLast 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.BeforeDays 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.MaxConcurrentDeletes 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.RemoveOrphanFilesEnable abc \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.BeforeDays 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.MaxConcurrentDeletes 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.MergeManifestsEnable abc \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.InheritDataBase abc \
    --TableBaseInfo.DbGovernPolicyIsDisable abc \
    --Columns.0.Name abc \
    --Columns.0.Type abc \
    --Columns.0.Comment abc \
    --Columns.0.Default abc \
    --Columns.0.NotNull True \
    --Partitions.0.Name abc \
    --Partitions.0.Type abc \
    --Partitions.0.Comment abc \
    --Partitions.0.PartitionType abc \
    --Partitions.0.PartitionFormat abc \
    --Partitions.0.PartitionDot 0 \
    --Partitions.0.Transform abc \
    --Partitions.0.TransformArgs abc \
    --Properties.0.Key abc \
    --Properties.0.Value abc \
    --UpsertKeys abc
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "<create sql>"
        },
        "RequestId": "RequestId"
    }
}
```

