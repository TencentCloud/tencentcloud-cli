**Example 1: 修改内容审核模板，开启画面令人反感信息的审核任务**

修改自定义 AI 内容审核模板。不指定过滤标签，将画面审核不适宜信息的任务判定为违规的分数阈值和画面审核任务判定为需要人工识别的分数阈值修改为默认。

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --Definition 30
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 修内容审核模板，开启画面不适宜的信息的审核任务并指定分数阈值**

修改自定义 AI 内容审核模板。不指定过滤标签，将画面令人反感的任务判定为违规的分数阈值修改为 90 分，将画面令人反感的任务判定为需要人工识别的分数阈值修改为 60 分。

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --PornConfigure.ImgReviewInfo.BlockConfidence 90 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.ReviewConfidence 60 \
    --Definition 30
```

Output: 
```
{
    "Response": {
        "RequestId": "82ae8d8e-dce3-4151-9d4b-5594145223e1"
    }
}
```

**Example 3: 修改内容审核模板，开启令人反感的信息的审核任务并指定过滤标签及分数阈值**

修改自定义 AI 内容审核模板。指定过滤标签为性感，将画面令人反感任务判定为违规的分数阈值修改为 90 分，将画面令人反感的任务判定为需要人工识别的分数阈值修改为 60 分。

Input: 

```
tccli vod ModifyContentReviewTemplate --cli-unfold-argument  \
    --PornConfigure.ImgReviewInfo.BlockConfidence 90 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.ReviewConfidence 60 \
    --PornConfigure.ImgReviewInfo.LabelSet sexy \
    --Definition 30
```

Output: 
```
{
    "Response": {
        "RequestId": "67ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

