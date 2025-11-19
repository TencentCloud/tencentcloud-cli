**Example 1: 绑定数据脱敏策略**



Input: 

```
tccli dlc AttachDataMaskPolicy --cli-unfold-argument  \
    --DataMaskStrategyPolicySet.0.PolicyInfo.Database default_database \
    --DataMaskStrategyPolicySet.0.PolicyInfo.Catalog DataLakeCatalog \
    --DataMaskStrategyPolicySet.0.PolicyInfo.Table default_table \
    --DataMaskStrategyPolicySet.0.PolicyInfo.Operation SELECT \
    --DataMaskStrategyPolicySet.0.PolicyInfo.PolicyType DATAMASK \
    --DataMaskStrategyPolicySet.0.PolicyInfo.Column string_msg \
    --DataMaskStrategyPolicySet.0.ColumnType string \
    --DataMaskStrategyPolicySet.0.DataMaskStrategyId 72de85e2-887a-4a87-bf86-90fc90ff25fa
```

Output: 
```
{
    "Response": {
        "RequestId": "12345678-1234-1234-1234-12345678"
    }
}
```

