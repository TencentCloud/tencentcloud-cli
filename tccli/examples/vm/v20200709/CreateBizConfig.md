**Example 1: 创建业务配置**

创建业务配置，1个账号最多可以创建20个配置

Input: 

```
tccli vm CreateBizConfig --cli-unfold-argument  \
    --BizType 1002 \
    --BizName 视频审核模板 \
    --ModerationCategories Porn Polity Terror \
    --MediaModeration.ImageFrequency 5 \
    --MediaModeration.AudioFrequency 60 \
    --MediaModeration.SegmentOutput.Bucket cms_segments-623322 \
    --MediaModeration.SegmentOutput.Region ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "c933aca1-90d2-4ab8-b045-f1b08069d76f"
    }
}
```

