**Example 1: 修改表**



Input: 

```
tccli cdwdoris UpdateTableSchema --cli-unfold-argument  \
    --InstanceId cdwdoris-7da9fxx \
    --DbName demo1 \
    --TableName tb1 \
    --Columns.0.Name name \
    --Columns.0.Type string \
    --Columns.0.AggType MIN \
    --Columns.0.IsNull False \
    --Columns.0.IsKey True \
    --Columns.0.DefaultValue bob \
    --Columns.0.IsPartition True \
    --Columns.0.IsDistribution False \
    --Columns.0.AutoInc False \
    --Columns.0.Comment 用户名称 \
    --Distribution.DistributionType Hash \
    --Distribution.Count 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx-xx-xx-xx-xx",
        "Success": true,
        "Message": "Table schema updated successfully."
    }
}
```

