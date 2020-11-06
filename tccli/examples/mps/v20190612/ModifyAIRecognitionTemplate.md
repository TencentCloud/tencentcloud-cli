**Example 1: 同时关闭和开启一项识别任务**

修改自定义视频内容识别模板，关闭文本全文识别任务，开启文本关键词识别任务。

Input: 

```
tccli mps ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --OcrFullTextConfigure.Switch OFF \
    --OcrWordsConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

