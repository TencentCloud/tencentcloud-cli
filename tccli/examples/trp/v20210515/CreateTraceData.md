**Example 1: 新增溯源信息**

新增溯源信息

Input: 

```
tccli trp CreateTraceData --cli-unfold-argument  \
    --TraceItems.0.Key name \
    --TraceItems.0.Name 名称 \
    --TraceItems.0.Value xltest \
    --TraceItems.0.Type text \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Hidden False \
    --TraceItems.0.Ext  \
    --TraceItems.1.Key avatar \
    --TraceItems.1.Name 主图 \
    --TraceItems.1.Value  \
    --TraceItems.1.Type image \
    --TraceItems.1.ReadOnly False \
    --TraceItems.1.Hidden False \
    --TraceItems.1.Values https://webcdn.m.qq.com/anxin/public/4054d20b71d30db847492eecc8057e90.jpg \
    --TraceItems.1.Ext  \
    --TraceItems.2.Key message \
    --TraceItems.2.Name 提示文本 \
    --TraceItems.2.Value 商品信息溯源详情 \
    --TraceItems.2.Type text \
    --TraceItems.2.ReadOnly False \
    --TraceItems.2.Hidden False \
    --TraceItems.2.Ext  \
    --TraceItems.3.Key desc \
    --TraceItems.3.Name 卡片描述 \
    --TraceItems.3.Value 二维码已完成扫码，请查看信息 \
    --TraceItems.3.Type text \
    --TraceItems.3.ReadOnly False \
    --TraceItems.3.Hidden False \
    --TraceItems.3.Ext  \
    --PhaseName 设计阶段 \
    --PhaseData.AppId  \
    --PhaseData.AppName  \
    --PhaseData.AppPath  \
    --PhaseData.HeadEnabled False \
    --PhaseData.HeadTitle  \
    --PhaseData.Key  \
    --Status 1 \
    --Type 1 \
    --Phase 2 \
    --ChainStatus 1 \
    --CorpId 10000
```

Output: 
```
{
    "Response": {
        "TraceId": "1mO3n3W0LDhAaADGwHjj3",
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

