**Example 1: 创建指定一项分析任务的模板**

创建一个自定义音视频内容分析模板，开启智能分类任务。

Input: 

```
tccli vod CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Comment 模板1 \
    --ClassificationConfigure.Switch ON \
    --Name 智能分析模板
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

**Example 2: 创建指定多项分析任务的模板**

创建一个自定义音视频内容分析模板，开启智能分类和智能标签任务。

Input: 

```
tccli vod CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Comment 模板2 \
    --TagConfigure.Switch ON \
    --ClassificationConfigure.Switch ON \
    --Name 智能分析模板
```

Output: 
```
{
    "Response": {
        "Definition": 31,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: 创建开启全部内容分析任务的模板**

创建一个自定义音视频内容分析模板，开启全部智能分析任务。

Input: 

```
tccli vod CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Comment 模板3 \
    --ClassificationConfigure.Switch ON \
    --Name 智能分析模板 \
    --TagConfigure.Switch ON \
    --FrameTagConfigure.Switch ON \
    --FrameTagConfigure.ScreenshotInterval 0.5 \
    --CoverConfigure.Switch NO
```

Output: 
```
{
    "Response": {
        "Definition": 33,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

