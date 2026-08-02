**Example 1: 修改主机 HostName 并重启**



Input: 

```
tccli dbdc ModifyDBCustomNodeAttributes --cli-unfold-argument  \
    --NodeId dbcn-qv204bsi \
    --HostName host-2026.07.30 \
    --NodeName host-2026.07.30
```

Output: 
```
{
    "Response": {
        "TaskId": 1760,
        "RequestId": "de4430f5-b00f-464e-850d-966d7d417993"
    }
}
```

