**Example 1: Replacing Tags Associated with a Resource with Input Tags**



Input: 

```
tccli tag ModifyResourceTags --cli-unfold-argument  \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123 \
    --ReplaceTags.0.TagKey testTagKey1 \
    --ReplaceTags.0.TagValue testTagValue1 \
    --ReplaceTags.1.TagKey testTagKey2 \
    --ReplaceTags.1.TagValue testTagValue2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: Unassociating Tags from a Resource**



Input: 

```
tccli tag ModifyResourceTags --cli-unfold-argument  \
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123 \
    --DeleteTags.0.TagKey testTagKey1 \
    --DeleteTags.1.TagKey testTagKey2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

