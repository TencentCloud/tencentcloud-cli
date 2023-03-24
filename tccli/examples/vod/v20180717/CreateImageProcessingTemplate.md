**Example 1: 创建240x240缩略图的图片即时处理模板**

创建240x240缩略图的图片即时处理模板。

Input: 

```
tccli vod CreateImageProcessingTemplate --cli-unfold-argument  \
    --Operations.0.Type Scale \
    --Operations.0.Scale.Type ShortEdgeFirst \
    --Operations.0.Scale.ShortEdge 240 \
    --Operations.1.Type CenterCut \
    --Operations.1.CenterCut.Type Rectangle \
    --Operations.1.CenterCut.Width 240 \
    --Operations.1.CenterCut.Height 240
```

Output: 
```
{
    "Response": {
        "Definition": 1009,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 创建短边缩放的图片即时处理模板**

创建短边缩放的图片即时处理模板。

Input: 

```
tccli vod CreateImageProcessingTemplate --cli-unfold-argument  \
    --Operations.0.Type Scale \
    --Operations.0.Scale.Type ShortEdgeFirst \
    --Operations.0.Scale.ShortEdge 120
```

Output: 
```
{
    "Response": {
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

