**Example 1: 测试样例**



Input: 

```
tccli mps CreateDocToVideoTask --cli-unfold-argument  \
    --Input.FileUrl https://aigc-test-image-1303333058.cos.ap-guangzhou.myqcloud***********************************************************6%96%AD-%E7%BB%84%E5%90%88%E6%8E%92%E5%88%971%E9%81%93.docx \
    --Input.Prompt 帮我生成一个视频，详细讲解文档中的内容。 \
    --Input.ModelName Wand \
    --Input.ModelVersion 1.0 \
    --Input.Ratio 16:9 \
    --Input.Language zh \
    --Input.EnableTTS True
```

Output: 
```
{
    "Response": {
        "TaskId": "e084efaa-d25************6b85e473c0e5",
        "RequestId": "a2644899-acbf-4973-b8ea-1a93772be6f7"
    }
}
```

