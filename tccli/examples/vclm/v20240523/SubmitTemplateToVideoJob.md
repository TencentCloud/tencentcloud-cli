**Example 1: 提交视频特效任务**



Input: 

```
tccli vclm SubmitTemplateToVideoJob --cli-unfold-argument  \
    --Template hug \
    --Images.0.Url https://cos-internal.ap-guangzhou.tencentcos.cn/templatetovideo/example.png
```

Output: 
```
{
    "Response": {
        "JobId": "1421389687608336384",
        "RequestId": "a81b4c44-c865-4ca1-ad69-08be3f63528c"
    }
}
```

