**Example 1: 提交审核任务**

业务侧将疑似违规的音频、视频、文本、图片等数据，通过此接口提交到腾讯审核平台，由后端专业人工审核团队进行审核校验。

Input: 

```
tccli cms ManualReview --cli-unfold-argument  \
    --ReviewContent.ContentId "123456" \
    --ReviewContent.Content "文本为Base64，其他类型提交URL" \
    --ReviewContent.ContentType 3 \
    --ReviewContent.AutoResult 0 \
    --ReviewContent.AutoDetailCode 20001 \
    --ReviewContent.BatchId "20200419_0001" \
    --ReviewContent.UserInfo "{}" \
    --ReviewContent.CreateTime 130000 \
    --ReviewContent.Priority 2 \
    --ReviewContent.CallBackInfo "" \
    --ReviewContent.Title ""
```

Output: 
```
{
    "Response": {
        "RequestId": "153e746d-d323-4042-b8ab-50b56ad54d36",
        "Data": {
            "ContentId": "123456",
            "BatchId": "20200419_0001"
        }
    }
}
```

