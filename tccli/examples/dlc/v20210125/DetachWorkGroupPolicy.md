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

**Example 2: 解绑工作组鉴权策略（TF场景）**



Input: 

```
tccli dlc DetachWorkGroupPolicy --cli-unfold-argument  \
    --WorkGroupId 221683 \
    --PolicyIds v1|WORKGROUP|221683|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER
```

Output: 
```
{
    "Response": {
        "RequestId": "8e98d880-156b-4151-9e06-38a5aa1bf010"
    }
}
```

