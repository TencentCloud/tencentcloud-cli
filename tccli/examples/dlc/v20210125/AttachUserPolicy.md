**Example 1: 绑定鉴权策略到用户**



Input: 

```
tccli dlc AttachUserPolicy --cli-unfold-argument  \
    --UserId 1248065439 \
    --PolicySet.0.Table TableName \
    --PolicySet.0.Catalog COSDataCatalog \
    --PolicySet.0.Operation ALL \
    --PolicySet.0.Database DatabaseName
```

Output: 
```
{
    "Response": {
        "RequestId": "1287310-badou889lodj-1231jk12"
    }
}
```

