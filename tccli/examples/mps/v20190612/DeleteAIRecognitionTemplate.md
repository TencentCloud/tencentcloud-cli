**Example 1: 删除模板 ID 为 30 的视频内容识别模板**

删除用户自定义视频内容识别模板。

Input: 

```
tccli mps DeleteAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30
```

Output: 
```
{
    "Response": {
        "RequestId": "35ae8d8e-dce3-42851-9d4b-559414529d931"
    }
}
```

