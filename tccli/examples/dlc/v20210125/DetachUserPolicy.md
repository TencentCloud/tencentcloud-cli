**Example 1: 解绑用户鉴权策略**



Input: 

```
tccli dlc DetachUserPolicy --cli-unfold-argument  \
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
        "RequestId": "79a91d1b-c00d-4b4f-b1da-0fbf339efa9a"
    }
}
```

