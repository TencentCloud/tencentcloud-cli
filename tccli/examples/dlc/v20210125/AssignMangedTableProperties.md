**Example 1: 示例一**

示例一

Input: 

```
tccli dlc AssignMangedTableProperties --cli-unfold-argument  \
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
    --TableBaseInfo.GovernPolicy.RuleType abc \
    --TableBaseInfo.GovernPolicy.GovernEngine abc \
    --TableBaseInfo.GovernPolicy.Mode 0 \
    --TableBaseInfo.GovernPolicy.PrimaryKeys abc \
    --TableBaseInfo.DbGovernPolicyIsDisable abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Uin abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.PolicyType abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Catalog abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Database abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Table abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.AppId abc \
    --TableBaseInfo.SmartPolicy.Policy.Inherit abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.AttributionType abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.ResourceType abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Name abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Instance abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Priority 0 \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Catalog abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.DataBase abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Table abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Status 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.WrittenEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CompactEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.DeleteEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.MinInputFiles 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.TargetFileSizeBytes 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RetainLast 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.BeforeDays 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.ExpiredSnapshotsIntervalMin 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RemoveOrphanIntervalMin 0 \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.LifecycleEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.Expiration 0 \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.DropTable True \
    --TableBaseInfo.SmartPolicy.Policy.Index.IndexEnable abc \
    --Columns.0.Name abc \
    --Columns.0.Type abc \
    --Columns.0.Comment abc \
    --Columns.0.Default abc \
    --Columns.0.NotNull True \
    --Columns.0.Precision 0 \
    --Columns.0.Scale 0 \
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
        "Properties": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

