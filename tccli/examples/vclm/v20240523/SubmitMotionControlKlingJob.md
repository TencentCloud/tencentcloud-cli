**Example 1: 调用成功示例**



Input: 

```
tccli vclm SubmitMotionControlKlingJob --cli-unfold-argument  \
    --Prompt 参考图任务动作和视频保持一致 \
    --Model kling-v3 \
    --Mode std \
    --CallbackUrl http://*********:8080 \
    --Image https://************************.cos.ap-guangzhou.myqcloud.com/********/video/motion-control/motion-control.jpg \
    --Video https://************************.cos.ap-guangzhou.myqcloud.com/********/video/motion-control/motion-control.mp4 \
    --KeepOriginalSound yes \
    --CharacterOrientation image
```

Output: 
```
{
    "Response": {
        "JobId": "1428569086702002176",
        "RequestId": "67f7771e-ebf2-49cf-ad5d-bd9fd1fa3724"
    }
}
```

