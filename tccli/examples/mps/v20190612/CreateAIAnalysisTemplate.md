**Example 1: 创建指定一项分析任务的模板**

创建一个自定义视频内容分析模板，开启智能分类任务。

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 智能分析模板 \
    --Comment 模板1 \
    --ClassificationConfigure.Switch ON
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

创建一个自定义视频内容分析模板，开启智能分类和智能标签任务。

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 智能分析模板 \
    --Comment 模板2 \
    --ClassificationConfigure.Switch ON \
    --TagConfigure.Switch ON
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

创建一个自定义视频内容分析模板，开启全部智能分析任务。

Input: 

```
tccli mps CreateAIAnalysisTemplate --cli-unfold-argument  \
    --Name 智能分析模板 \
    --Comment 模板3 \
    --ClassificationConfigure.Switch ON \
    --TagConfigure.Switch ON \
    --CoverConfigure.Switch NO \
    --FrameTagConfigure.Switch ON
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

