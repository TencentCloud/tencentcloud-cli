**Example 1: 变更备可用区**



Input: 

```
tccli cynosdb ModifyClusterSlaveZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --OldSlaveZone ap-guangzhou-2 \
    --NewSlaveZone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "FlowId": 123,
        "RequestId": "128046"
    }
}
```

