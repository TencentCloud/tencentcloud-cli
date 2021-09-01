**Example 1: 发起主动回收只读组**



Input: 

```
tccli sqlserver RecycleReadOnlyGroup --cli-unfold-argument  \
    --InstanceId mssql-2cwisu23 \
    --ReadOnlyGroupId mssqlrg-787oxy95
```

Output: 
```
{
    "Response": {
        "FlowId": 1001539,
        "RequestId": "e092520d-86c3-46ba-a39d-dc1373b7a82d"
    }
}
```

