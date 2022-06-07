**Example 1: 新增溯源信息**

新增溯源信息

Input: 

```
tccli trp CreateTraceData --cli-unfold-argument  \
    --TraceItems.0.Name xx \
    --TraceItems.0.Value xx \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Values xx \
    --TraceItems.0.Hidden True \
    --TraceItems.0.Type xx \
    --TraceItems.1.Name xx \
    --TraceItems.1.Value xx \
    --TraceItems.1.ReadOnly True \
    --TraceItems.1.Values https://webcdn.m.qq.com/dpsw/cdn/1653cdd0ba37ee5faa421c8a0adfab0d.jpg \
    --TraceItems.1.Hidden True \
    --TraceItems.1.Type xx \
    --BatchId xx \
    --PhaseName xx \
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

