**Example 1: 示例**



Input: 

```
tccli clouddc CreateLead --cli-unfold-argument  \
    --Contributor 12334556 \
    --SourcePrimaryTagId 123 \
    --SourceSecondaryTagId 123 \
    --Qq 123 \
    --Phone 18888888888 \
    --Name 123 \
    --Email 123@qq.com \
    --BatchId 123 \
    --LeadReleaseSource 123 \
    --LeadReleaseSourceId 123 \
    --BelongModule 1 \
    --Extend.0.KeyName xx \
    --Extend.0.KeyValue xx \
    --Extend.0.Key xx
```

Output: 
```
{
    "Response": {
        "JsonString": "{\"leadId\":50}",
        "RequestId": "25ede15b-f30e-4f5f-8356-c38db98cfa23"
    }
}
```

