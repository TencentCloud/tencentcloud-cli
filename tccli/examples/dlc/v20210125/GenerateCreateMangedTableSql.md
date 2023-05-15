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

