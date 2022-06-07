**Example 1: 修改溯源信息**



Input: 

```
tccli trp ModifyTraceData --cli-unfold-argument  \
    --TraceItems.0.Name xx \
    --TraceItems.0.Value xx \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Values xx \
    --TraceItems.0.Hidden True \
    --TraceItems.0.Type xx \
    --BatchId xx \
    --Code xx \
    --PhaseName xx \
    --TaskId xx \
    --Phase 1
```

Output: 
```
{
    "Response": {
        "TraceId": "xx",
        "RequestId": "xx"
    }
}
```

