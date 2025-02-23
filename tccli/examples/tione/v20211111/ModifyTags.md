**Example 1: 标记服务组标签**



Input: 

```
tccli tione ModifyTags --cli-unfold-argument  \
    --ServiceGroupId abc-1234 \
    --Tags.0.TagKey author \
    --Tags.0.TagValue allen \
    --ServiceCategory TAIJI_HY
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-1234"
    }
}
```

