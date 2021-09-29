**Example 1: 绑定鉴权策略到工作组**



Input: 

```
tccli dlc AttachWorkGroupPolicy --cli-unfold-argument  \
    --WorkGroupId 112 \
    --PolicySet.0.Table TableName \
    --PolicySet.0.Catalog COSDataCatalog \
    --PolicySet.0.Operation ALL \
    --PolicySet.0.Database DatabaseName
```

Output: 
```
{
    "Response": {
        "RequestId": "0ebb0fdc-0cbd-4408-9f08-ee75a7d6d80f"
    }
}
```

