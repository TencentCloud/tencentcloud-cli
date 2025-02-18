**Example 1: p_cdn查询明细流水_结果压缩**



Input: 

```
tccli billing DescribeMeasureDetailListCompress --cli-unfold-argument  \
    --ProductCode p_cdn \
    --DosageType request_cdn_https \
    --DosageVersion 1 \
    --StartTime 2024-09-24 00:00:00 \
    --EndTime 2024-12-24 23:59:59 \
    --DetailName domain1Min \
    --PageSize 100 \
    --PageToken  \
    --Attribute.0.Name area \
    --Attribute.0.Value 1000 \
    --Attribute.1.Name realm \
    --Attribute.1.Value 1
```

Output: 
```
{
    "Response": {
        "Data": "H4sIAAAAAAAAAKtWCkhMTw3Jz07NU7JSUtJRckktSczM8cksLlGyio6tBQDcDY01IAAAAA==",
        "RequestId": "a0438d20-cd99-4af8-8872-68364616a789"
    }
}
```

