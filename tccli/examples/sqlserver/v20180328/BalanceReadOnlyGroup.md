**Example 1: 按照默认权重平衡只读组中的只读副本**



Input: 

```
tccli sqlserver BalanceReadOnlyGroup --cli-unfold-argument  \
    --InstanceId mssql-2cwisu23 \
    --ReadOnlyGroupId mssqlrg-itaunotj
```

Output: 
```
{
    "Response": {
        "RequestId": "9b3c49f5-0e04-4b1a-98eb-43d464424354"
    }
}
```

