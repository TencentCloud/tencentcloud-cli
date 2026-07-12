**Example 1: 解绑用户鉴权策略**



Input: 

```
tccli dlc DetachUserPolicy --cli-unfold-argument  \
    --UserId 100045074431 \
    --PolicySet.0.Database test_ykz_db \
    --PolicySet.0.Catalog DataLakeCatalog \
    --PolicySet.0.Table * \
    --PolicySet.0.Operation ALL \
    --PolicySet.0.PolicyType TABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "d2cdc1f3-89cb-4719-a362-1cec464fbb78"
    }
}
```

**Example 2: 解绑用户鉴权策略（TF场景）**



Input: 

```
tccli dlc DetachUserPolicy --cli-unfold-argument  \
    --UserId 700002810925 \
    --PolicyIds v1|USER|700002810925|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER
```

Output: 
```
{
    "Response": {
        "RequestId": "05758b51-45e0-44a3-a6e5-77d6ee6e58d3"
    }
}
```

