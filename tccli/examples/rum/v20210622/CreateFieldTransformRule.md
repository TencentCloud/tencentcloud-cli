**Example 1: CreateFieldTransformRule示例**



Input: 

```
tccli rum CreateFieldTransformRule --cli-unfold-argument  \
    --ProjectId 146662 \
    --TargetField page_url \
    --MatchType exact1 \
    --MatchPattern mall \
    --TransformAction replace \
    --Name replace \
    --ReplaceValue m**l \
    --Priority 1 \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"invalid match_type: exact1, allowed: exact, prefix, contains, regex\"}",
        "RequestId": "96774c45-9e84-4d48-8f5d-3c4d09f2007c"
    }
}
```

