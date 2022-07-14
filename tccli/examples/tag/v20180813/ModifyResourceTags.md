**Example 1: 将资源关联的标签替换为输入的标签集合**



Input: 

```
tccli tag ModifyResourceTags --cli-unfold-argument  \
    --ReplaceTags.0.TagKey testTagKey2 \
    --ReplaceTags.0.TagValue testTagValue2 \
    --ReplaceTags.1.TagKey testTagKey1 \
    --ReplaceTags.1.TagValue testTagValue1 \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 给资源解除绑定多个标签**



Input: 

```
tccli tag ModifyResourceTags --cli-unfold-argument  \
    --DeleteTags.0.TagKey testTagKey2 \
    --DeleteTags.1.TagKey testTagKey1 \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

