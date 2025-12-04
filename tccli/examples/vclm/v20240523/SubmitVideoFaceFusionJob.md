**Example 1: 提交视频人脸融合任务**



Input: 

```
tccli vclm SubmitVideoFaceFusionJob --cli-unfold-argument  \
    --VideoUrl https://cos.ap-guangzhou.myqcloud.com/facefusion/face/video2.mp4 \
    --TemplateInfos.0.TemplateFaceID 0 \
    --TemplateInfos.0.TemplateFaceImage.Url https://cos.ap-guangzhou.myqcloud.com/facefusion/face/face.png \
    --MergeInfos.0.MergeFaceImage.Url https://cos.ap-guangzhou.myqcloud.com/facefusion/face/guodegang.jpg \
    --MergeInfos.0.TemplateFaceID 0
```

Output: 
```
{
    "Response": {
        "JobId": "1383749921168539648",
        "RequestId": "de9cc0c9-2acb-400f-8986-c29e22c92a60"
    }
}
```

