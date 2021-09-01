**Example 1: 创建索引**



Input: 

```
tccli cls CreateIndex --cli-unfold-argument  \
    --TopicId 3edc8551-111b-473b-9fc4-ed66e20dfa8a \
    --Status True \
    --Rule.FullText.CaseSensitive True \
    --Rule.FullText.Tokenizer * \
    --Rule.KeyValue.CaseSensitive True \
    --Rule.KeyValue.KeyValues.0.Key age \
    --Rule.KeyValue.KeyValues.0.Value.Type long \
    --Rule.KeyValue.KeyValues.0.Value.Tokenizer _ \
    --Rule.KeyValue.KeyValues.0.Value.SqlFlag False \
    --Rule.Tag.CaseSensitive True \
    --Rule.Tag.KeyValues.0.Key tag \
    --Rule.Tag.KeyValues.0.Value.Type string \
    --Rule.Tag.KeyValues.0.Value.Tokenizer ** \
    --Rule.Tag.KeyValues.0.Value.SqlFlag False
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

