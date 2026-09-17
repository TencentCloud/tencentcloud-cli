**Example 1: 测试样例**



Input: 

```
tccli mps CreateDocToVideoTask --cli-unfold-argument  \
    --Input.FileUrl https://aigc-tes**************************************************************************sample_min.docx \
    --Input.Prompt 根据文档内容，帮我生成一个视频 \
    --Input.ModelName WAND \
    --Input.ModelVersion 1.0-lite \
    --Input.Ratio 1:1 \
    --Input.ReferenceDuration 15 \
    --Input.EnableTTS True \
    --Input.PPTXFidelity False \
    --Input.Mode auto \
    --Input.EnableCaption False \
    --ResourceId vts-********-1
```

Output: 
```
{
    "Response": {
        "TaskId": "516e11a9-**************-e0c84dffda8b",
        "RequestId": "825f6082-c99b-455a-97a6-97bb56740cbe"
    }
}
```

