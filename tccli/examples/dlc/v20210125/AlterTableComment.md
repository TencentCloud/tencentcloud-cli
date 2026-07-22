**Example 1: 修改表备注**



Input: 

```
tccli dlc AlterTableComment --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName abc \
    --TableBaseInfo.TableName abc \
    --TableBaseInfo.DatasourceConnectionName abc \
    --TableBaseInfo.TableComment abc \
    --TableBaseInfo.Type abc \
    --TableBaseInfo.TableFormat abc \
    --TableBaseInfo.UserAlias abc \
    --TableBaseInfo.UserSubUin abc \
    --TableBaseInfo.GovernPolicy.RuleType abc \
    --TableBaseInfo.GovernPolicy.GovernEngine abc \
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
    --TableBaseInfo.SmartPolicy.Policy.Index.IndexEnable abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

