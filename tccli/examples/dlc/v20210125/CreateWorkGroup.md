**Example 1: 创建工作组**



Input: 

```
tccli dlc CreateWorkGroup --cli-unfold-argument  \
    --WorkGroupName Group1 \
    --WorkGroupDescription testGroup \
    --PolicySet.0.Table TableName \
    --PolicySet.0.Catalog COSDataCatalog \
    --PolicySet.0.Operation ALL \
    --PolicySet.0.Database DatabaseName
```

Output: 
```
{
    "Response": {
        "WorkGroupId": 1,
        "RequestId": "1287310-badou889lodj-1231jk12"
    }
}
```

