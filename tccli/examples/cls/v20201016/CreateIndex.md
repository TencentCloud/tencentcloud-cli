**Example 1: 创建索引**



Input: 

```
tccli cls CreateIndex --cli-unfold-argument  \
    --TopicId 75f531f6-3644-45e5-8717-af1dc294cc93 \
    --Status True \
    --Rule.FullText.CaseSensitive True \
    --Rule.FullText.Tokenizer @&?|#()='",;:<>[]{}/ 
	\ \
    --Rule.KeyValue.CaseSensitive True \
    --Rule.KeyValue.KeyValues.0.Key age \
    --Rule.KeyValue.KeyValues.0.Value.Type long \
    --Rule.KeyValue.KeyValues.0.Value.Tokenizer  \
    --Rule.KeyValue.KeyValues.0.Value.SqlFlag False \
    --Rule.Tag.CaseSensitive True \
    --Rule.Tag.KeyValues.0.Key tag \
    --Rule.Tag.KeyValues.0.Value.Type text \
    --Rule.Tag.KeyValues.0.Value.Tokenizer @&?|#()='",;:<>[]{}/ 
	\ \
    --Rule.Tag.KeyValues.0.Value.SqlFlag False
```

Output: 
```
{
    "Response": {
        "RequestId": "8d3c9e9e-0c2f-4d9a-bb17-71e4f42f89fd"
    }
}
```

