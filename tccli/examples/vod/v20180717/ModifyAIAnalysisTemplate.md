**Example 1: 关闭智能封面任务**

修改自定义音视频内容分析模板，关闭智能封面任务。

Input: 

```
tccli vod ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --Definition 30 \
    --CoverConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 开启智能封面任务**

修改自定义音视频内容分析模板，开启智能封面任务。

Input: 

```
tccli vod ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --Definition 30 \
    --CoverConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: 同时开启一项和关闭一项内容分析任务**

修改自定义音视频内容分析模板，开启智能标签任务，关闭智能封面任务。

Input: 

```
tccli vod ModifyAIAnalysisTemplate --cli-unfold-argument  \
    --TagConfigure.Switch ON \
    --Definition 30 \
    --CoverConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

