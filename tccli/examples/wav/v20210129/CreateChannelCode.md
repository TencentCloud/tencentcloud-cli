**Example 1: 渠道活码创建实例**



Input: 

```
tccli wav CreateChannelCode --cli-unfold-argument  \
    --Remark 如图 \
    --AppIds DEFAULT \
    --Name 测试企业标签的活码 \
    --UseUserId 1386218784692961300 \
    --SourceName 自然到店 \
    --MsgId 1397103192673538050 \
    --Source 1 \
    --Tag.0.BizTagIdStr 1394843909254754300 \
    --Tag.0.BizTagId 1394843909254754300 \
    --Tag.0.BizGroupId 1394843720913727500 \
    --Tag.0.TagId etQIM2CwAA_dZ7TUzES2iRRIGXJrWY8w \
    --Tag.0.GroupName 测试111 \
    --Tag.0.TagName 额嗡嗡嗡 \
    --Tag.0.Type 1 \
    --SkipVerify 0 \
    --UseUserOpenId 544064e019b53e4791115020ffc68f33 \
    --Type 1 \
    --SourceType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "fea177dd-9fa6-4e76-9c8f-67f5a21f20bb"
    }
}
```

