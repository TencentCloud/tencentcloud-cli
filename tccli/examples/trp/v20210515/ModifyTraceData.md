**Example 1: 修改溯源信息**

修改部分溯源信息

Input: 

```
tccli trp ModifyTraceData --cli-unfold-argument  \
    --TraceId 1mO3n3W0LDhAaADGwHjj3 \
    --BatchId 20241022112952826 \
    --TaskId 2021091500001 \
    --TraceItems.0.Key name \
    --TraceItems.0.Name 名称 \
    --TraceItems.0.Value xltest \
    --TraceItems.0.Type text \
    --TraceItems.0.ReadOnly True \
    --TraceItems.0.Hidden False \
    --TraceItems.1.Key avatar \
    --TraceItems.1.Name 主图 \
    --TraceItems.1.Value  \
    --TraceItems.1.Type image \
    --TraceItems.1.ReadOnly False \
    --TraceItems.1.Hidden False \
    --TraceItems.1.Values https://webcdn.m.qq.com/anxin/public/4054d20b71d30db847492eecc8057e90.jpg \
    --TraceItems.2.Key message \
    --TraceItems.2.Name 提示文本 \
    --TraceItems.2.Value 商品信息溯源详情 \
    --TraceItems.2.Type text \
    --TraceItems.2.ReadOnly False \
    --TraceItems.2.Hidden False \
    --TraceItems.3.Key desc \
    --TraceItems.3.Name 卡片描述 \
    --TraceItems.3.Value 二维码已完成扫码，请查看信息 \
    --TraceItems.3.Type text \
    --TraceItems.3.ReadOnly False \
    --TraceItems.3.Hidden False \
    --PhaseName 设计阶段 \
    --PhaseData.AppId  \
    --PhaseData.AppName  \
    --PhaseData.AppPath  \
    --PhaseData.HeadEnabled False \
    --PhaseData.HeadTitle  \
    --PhaseData.Key  \
    --Status 1 \
    --Rank 1 \
    --Type 1 \
    --Code https://anxin.qq.com/q99j9ovp5c6sok7l5g \
    --Phase 2 \
    --TraceTime 2024-10-30T07:16:21.265Z \
    --CreateTime 2024-10-30T07:16:21.265Z \
    --ChainStatus 1 \
    --ChainTime 2024-10-30T07:16:21.265Z \
    --ChainData.BlockTime 2024-03-27T03:33:21.000Z \
    --ChainData.BlockHash 129fd196158b497b88bcb02ac7b34f3729c806e925074b448bad35f3da960072 \
    --ChainData.BlockHeight 684 \
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

