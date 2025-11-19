**Example 1: 绑定鉴权策略到用户**



Input: 

```
tccli dlc AttachUserPolicy --cli-unfold-argument  \
    --UserId 10401463674518 \
    --PolicySet.0.Database create_test \
    --PolicySet.0.Catalog DataLakeCatalog \
    --PolicySet.0.Operation CREATE_TABLE \
    --PolicySet.0.Table test_table \
    --PolicySet.0.PolicyType TABLE \
    --PolicySet.0.Mode SENIOR
```

Output: 
```
{
    "Response": {
        "RequestId": "4e2a0b4b-6c0b-40de-9e39-0761ed1f6be4"
    }
}
```

