**Example 1: 修改只读组详情**



Input: 

```
tccli sqlserver ModifyReadOnlyGroupDetails --cli-unfold-argument  \
    --InstanceId mssql-6f4ddx2f \
    --ReadOnlyGroupId mssqlrg-552tyamb \
    --ReadOnlyGroupName change_name \
    --IsOfflineDelay 1 \
    --ReadOnlyMaxDelayTime 18 \
    --MinReadOnlyInGroup 1 \
    --AutoWeight 0 \
    --BalanceWeight 1 \
    --WeightPairs.0.ReadOnlyInstanceId mssqlro-5k508n7p \
    --WeightPairs.0.ReadOnlyWeight 50 \
    --WeightPairs.1.ReadOnlyInstanceId mssqlro-91masbl1 \
    --WeightPairs.1.ReadOnlyWeight 50
```

Output: 
```
{
    "Response": {
        "RequestId": "4db4cc07-920a-4d04-8627-d45c582e96e7"
    }
}
```

