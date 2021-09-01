**Example 1: ModifyDBInstanceReadOnlyGroup**



Input: 

```
tccli postgres ModifyDBInstanceReadOnlyGroup --cli-unfold-argument  \
    --DBInstanceId postgres-k95qzetn \
    --NewReadOnlyGroupId NewGroup \
    --ReadOnlyGroupId OldGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8",
        "FlowId": 912
    }
}
```

