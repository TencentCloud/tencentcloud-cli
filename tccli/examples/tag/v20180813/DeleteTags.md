**Example 1: 删除标签**



Input: 

```
tccli tag DeleteTags --cli-unfold-argument  \
    --Tags.0.TagKey 09221 \
    --Tags.0.TagValue 092211 \
    --Tags.1.TagKey 09221 \
    --Tags.1.TagValue 092212
```

Output: 
```
{
    "Response": {
        "RequestId": "131fd253-b2de-4190-a1c1-13ce*********"
    }
}
```

