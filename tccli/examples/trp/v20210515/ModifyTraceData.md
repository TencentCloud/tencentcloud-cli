**Example 1: 修改溯源信息**

修改部分溯源信息

Input: 

```
tccli trp ModifyTraceData --cli-unfold-argument  \
    --TraceId abc \
    --BatchId abc \
    --TaskId abc \
    --TraceItems.0.Name abc \
    --TraceItems.0.Value abc \
    --TraceItems.0.Type abc \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Hidden True \
    --TraceItems.0.Values abc \
    --TraceItems.0.Key abc \
    --TraceItems.0.Ext abc \
    --TraceItems.0.Attrs.Name abc \
    --TraceItems.0.Attrs.Value abc \
    --TraceItems.0.Attrs.Type abc \
    --TraceItems.0.Attrs.ReadOnly True \
    --TraceItems.0.Attrs.Hidden True \
    --TraceItems.0.Attrs.Values abc \
    --TraceItems.0.Attrs.Key abc \
    --TraceItems.0.Attrs.Ext abc \
    --TraceItems.0.Attrs.Attrs.Name abc \
    --TraceItems.0.Attrs.Attrs.Value abc \
    --TraceItems.0.Attrs.Attrs.Type abc \
    --TraceItems.0.Attrs.Attrs.ReadOnly True \
    --TraceItems.0.Attrs.Attrs.Hidden True \
    --TraceItems.0.Attrs.Attrs.Values abc \
    --TraceItems.0.Attrs.Attrs.Key abc \
    --TraceItems.0.Attrs.Attrs.Ext abc \
    --PhaseName abc \
    --PhaseData.HeadEnabled True \
    --PhaseData.HeadTitle abc \
    --PhaseData.Key abc \
    --PhaseData.AppId abc \
    --PhaseData.AppPath abc \
    --PhaseData.AppName abc \
    --Status 1 \
    --Rank 1 \
    --Type 1 \
    --Code abc \
    --Phase 1 \
    --TraceTime abc \
    --CreateTime abc \
    --ChainStatus 1 \
    --ChainTime abc \
    --ChainData.BlockHash abc \
    --ChainData.BlockHeight abc \
    --ChainData.BlockTime abc \
    --CorpId 1
```

Output: 
```
{
    "Response": {
        "TraceId": "abc",
        "RequestId": "abc"
    }
}
```

