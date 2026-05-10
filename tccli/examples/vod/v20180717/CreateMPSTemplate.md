**Example 1: 创建 MPS 智能分析模板**



Input: 

```
tccli vod CreateMPSTemplate --cli-unfold-argument  \
    --SubAppId 260085028 \
    --TemplateType AIAnalysis \
    --AIAnalysisTemplate.Name 智能分析 \
    --AIAnalysisTemplate.Comment 智能分析模版 \
    --AIAnalysisTemplate.ClassificationConfigure.Switch ON \
    --AIAnalysisTemplate.TagConfigure.Switch ON \
    --AIAnalysisTemplate.CoverConfigure.Switch ON \
    --AIAnalysisTemplate.FrameTagConfigure.Switch ON \
    --AIAnalysisTemplate.SplitConfigure.Switch ON \
    --AIAnalysisTemplate.HighlightConfigure.Switch ON \
    --AIAnalysisTemplate.OpeningAndEndingConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 30186,
        "RequestId": "c6d3e3f5-1082-4053-89e0-4172b456c2e1"
    }
}
```

