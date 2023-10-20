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
        "Execution": {
            "SQL": "<create sql>"
        },
        "RequestId": "RequestId"
    }
}
```

