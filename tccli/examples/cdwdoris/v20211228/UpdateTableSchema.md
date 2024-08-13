**Example 1: 修改表**



Input: 

```
tccli cdwdoris UpdateTableSchema --cli-unfold-argument  \
    --InstanceId abc \
    --UserName abc \
    --PassWord abc \
    --DbName abc \
    --TableName abc \
    --Columns.0.Name abc \
    --Columns.0.Type abc \
    --Columns.0.AggType abc \
    --Columns.0.IsNull True \
    --Columns.0.IsKey True \
    --Columns.0.DefaultValue abc \
    --Columns.0.IsPartition True \
    --Columns.0.IsDistribution True \
    --Columns.0.AutoInc True \
    --Columns.0.Comment abc \
    --IndexInfos.0.IdxName abc \
    --IndexInfos.0.ColumnName abc \
    --IndexInfos.0.IdxType abc \
    --IndexInfos.0.IdxProperties.0.PropertyKey abc \
    --IndexInfos.0.IdxProperties.0.PropertyValue abc \
    --IndexInfos.0.IdxComment abc \
    --Distribution.DistributionType abc \
    --Distribution.Count 0 \
    --TableComment abc \
    --Properties.0.PropertyKey abc \
    --Properties.0.PropertyValue abc
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

