**Example 1: ModifyFieldTransformRule示例**



Input: 

```
tccli rum ModifyFieldTransformRule --cli-unfold-argument  \
    --Id 4 \
    --ProjectId 146662 \
    --Name fieldName \
    --TargetField page_url \
    --MatchType contains \
    --MatchPattern mall \
    --TransformAction replace \
    --ReplaceValue replace \
    --Priority 1 \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "Result": "{\"Rule\":{\"CreatedAt\":\"2026-04-12T08:38:03Z\",\"CreatedBy\":\"700001860566\",\"Enabled\":true,\"Id\":4,\"MatchPattern\":\"mall\",\"MatchType\":\"contains\",\"Name\":\"fieldName\",\"Priority\":1,\"ProjectId\":146662,\"ReplaceValue\":\"replace\",\"TargetField\":\"page_url\",\"TransformAction\":\"replace\",\"UpdatedAt\":\"2026-04-20T16:48:30.65+08:00\",\"UpdatedBy\":\"600000563898\"}}",
        "RequestId": "60381ca9-6934-4eb8-9ae4-c9ef2cbc0193"
    }
}
```

