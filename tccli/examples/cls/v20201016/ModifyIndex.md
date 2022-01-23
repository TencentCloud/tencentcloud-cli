**Example 1: 修改索引**



Input: 

```
tccli cls ModifyIndex --cli-unfold-argument  \
    --TopicId 826f8b26-b054-4a0d-8c8e-f3d609f5e0ea \
    --Rule.FullText.CaseSensitive False \
    --Rule.FullText.Tokenizer -=/? \
    --Rule.Tag.CaseSensitive False \
    --Rule.Tag.KeyValues.0.Value.Type long \
    --Rule.Tag.KeyValues.0.Value.SqlFlag True \
    --Rule.Tag.KeyValues.0.Key timestamp \
    --Rule.KeyValue.CaseSensitive False \
    --Rule.KeyValue.KeyValues.0.Value.Type long \
    --Rule.KeyValue.KeyValues.0.Value.SqlFlag True \
    --Rule.KeyValue.KeyValues.0.Key age \
    --Status True
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

