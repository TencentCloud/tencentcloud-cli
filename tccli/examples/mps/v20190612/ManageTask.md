**Example 1: Terminating specified live stream processing task**



Input: 

```
tccli mps ManageTask --cli-unfold-argument  \
    --OperationType Abort \
    --TaskId 2459149217-procedure-live-xxx51da009t0
```

Output: 
```
{
    "Response": {
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5"
    }
}
```

