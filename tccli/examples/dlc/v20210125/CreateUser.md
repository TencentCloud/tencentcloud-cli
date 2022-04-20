**Example 1: 创建用户**



Input: 

```
tccli dlc CreateUser --cli-unfold-argument  \
    --UserDescription Test User \
    --UserAlias Testname \
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

