**Example 1: 渠道活码创建实例**



Input: 

```
tccli wav CreateChannelCode --cli-unfold-argument  \
    --Remark xx \
    --AppIds xx \
    --Name xx \
    --UseUserId 0 \
    --SourceName xx \
    --MsgId 0 \
    --Source xx \
    --Tag.0.BizTagIdStr xx \
    --Tag.0.BizTagId 0 \
    --Tag.0.BizGroupId 0 \
    --Tag.0.TagId xx \
    --Tag.0.GroupName xx \
    --Tag.0.TagName xx \
    --Tag.0.Type 0 \
    --SkipVerify 0 \
    --UseUserOpenId xx \
    --Type 0 \
    --SourceType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

