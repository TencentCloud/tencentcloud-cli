**Example 1: 修改从可用区**



Input: 

```
tccli cynosdb ModifyClusterSlaveZone --cli-unfold-argument  \
    --ClusterId xx \
    --OldSlaveZone xx \
    --NewSlaveZone xxx
```

Output: 
```
{
    "Response": {
        "FlowId": "123",
        "RequestId": "128046"
    }
}
```

