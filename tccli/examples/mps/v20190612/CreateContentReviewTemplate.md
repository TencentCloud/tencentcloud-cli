**Example 1: 创建开启画面令人反感的信息的内容识别模板，并指定过滤标签**

创建一个自定义 AI 内容审核模板，开启画面内容令人反感的信息任务，指定过滤标签为涉黄及性感，判定为违规的分数阈值及判定为需要人工识别的分数阈值都为默认。

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 内容审核模块 \
    --Comment 模板1 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.LabelSet porn sexy
```

Output: 
```
{
    "Response": {
        "Definition": 33,
        "RequestId": "67aee3e9-2qd3-2395-9d4b-4390a96837a7"
    }
}
```

**Example 2: 创建仅开启画面令人反感的信息的内容审核模板**

创建一个自定义 AI 内容审核模板，仅开启画面内容令人反感的信息任务，判定为违规的分数阈值和判定为需要人工识别的分数阈值都为默认值，不指定过滤标签。

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 内容审核模板 \
    --Comment 模板1 \
    --PornConfigure.ImgReviewInfo.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 30,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: 创建仅开启画面令人反感的信息的任务内容审核模板，并指定分数阈值和截帧间隔**

创建一个自定义 AI 内容审核模板，开启画面内容令人反感的信息任务，指定判定为画面违规的分数阈值为 80 分，判定为画面需要人工识别的阈值分数为 30 分。

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 内容审核模板 \
    --Comment 模板2 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --PornConfigure.ImgReviewInfo.BlockConfidence 80 \
    --PornConfigure.ImgReviewInfo.ReviewConfidence 30
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "97aee3e9-2qd3-4151-9d4b-9730a45227a9"
    }
}
```

**Example 4: 创建开启多项识别任务的内容审核模板**

创建一个自定义 AI 内容审核模板，开启画面内容令人反感的信息任务，同时开启画面令人不安全的信息及画面令人不适宜的信息任务，判定为违规的分数阈值及判定为需要人工识别的分数阈值都为默认，且不指定过滤标签。

Input: 

```
tccli mps CreateContentReviewTemplate --cli-unfold-argument  \
    --Name 内容审核模板 \
    --Comment 模板3 \
    --PornConfigure.ImgReviewInfo.Switch ON \
    --TerrorismConfigure.ImgReviewInfo.Switch ON \
    --TerrorismConfigure.OcrReviewInfo.Switch OFF \
    --PoliticalConfigure.ImgReviewInfo.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 32,
        "RequestId": "88aee3e9-2qd3-4151-9d4b-4390a45227a9"
    }
}
```

