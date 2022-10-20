**Example 1: 修改溯源信息**



Input: 

```
tccli trp ModifyTraceData --cli-unfold-argument  \
    --Status 1 \
    --ChainStatus 1 \
    --TraceId xx \
    --PhaseData.HeadTitle xx \
    --PhaseData.AppName xx \
    --PhaseData.AppPath xx \
    --PhaseData.Key xx \
    --PhaseData.AppId xx \
    --PhaseData.HeadEnabled False \
    --TraceTime xx \
    --TraceItems.0.Name xx \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Value xx \
    --TraceItems.0.Ext xx \
    --TraceItems.0.Values xx \
    --TraceItems.0.Key xx \
    --TraceItems.0.Hidden True \
    --TraceItems.0.Type xx \
    --Rank 1 \
    --BatchId xx \
    --ChainTime xx \
    --Code xx \
    --PhaseName xx \
    --TaskId xx \
    --CorpId 1 \
    --Phase 1 \
    --ChainData.BlockHeight xx \
    --ChainData.BlockHash xx \
    --ChainData.BlockTime xx \
    --Type 1 \
    --CreateTime xx
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

