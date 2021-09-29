**Example 1: 解绑工作组鉴权策略**



Input: 

```
tccli dlc DetachWorkGroupPolicy --cli-unfold-argument  \
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
        "RequestId": "94899a6b-a3e0-4d61-ad83-b51cb2473305"
    }
}
```

