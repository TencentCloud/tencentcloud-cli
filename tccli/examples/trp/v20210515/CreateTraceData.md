**Example 1: 新增溯源信息**

新增溯源信息

Input: 

```
tccli trp CreateTraceData --cli-unfold-argument  \
    --Status 1 \
    --ChainStatus 1 \
    --TraceId xx \
    --PhaseData.HeadTitle xx \
    --PhaseData.AppName xx \
    --PhaseData.AppPath xx \
    --PhaseData.Key xx \
    --PhaseData.AppId xx \
    --PhaseData.HeadEnabled False \
    --CorpId 1 \
    --TraceItems.0.Name xx \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Value xx \
    --TraceItems.0.Ext xx \
    --TraceItems.0.Values xx \
    --TraceItems.0.Key xx \
    --TraceItems.0.Hidden True \
    --TraceItems.0.Type xx \
    --TraceItems.1.Name xx \
    --TraceItems.1.ReadOnly True \
    --TraceItems.1.Value xx \
    --TraceItems.1.Ext xx \
    --TraceItems.1.Values https://webcdn.m.qq.com/dpsw/cdn/xxx.jpg \
    --TraceItems.1.Key xx \
    --TraceItems.1.Hidden True \
    --TraceItems.1.Type xx \
    --BatchId xx \
    --PhaseName xx \
    --TaskId xx \
    --Phase 1 \
    --Type 1
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

