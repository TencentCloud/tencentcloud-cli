**Example 1: 更新行过滤策略信息**



Input: 

```
tccli dlc UpdateRowFilter --cli-unfold-argument  \
    --Policy.Table TableName \
    --Policy.Catalog COSDataCatalog \
    --Policy.Operation ALL \
    --Policy.Database DatabaseName \
    --PolicyId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1287310-badou889lodj-1231jk12"
    }
}
```

