**Example 1: 创建文件识别任务示例**

创建文件识别任务示例

Input: 

```
tccli ocr CreateAIFormTask --cli-unfold-argument  \
    --FileList.0.FileUrl https://xxx.jpg \
    --FileList.0.FileOrderNumber 1 \
    --FileList.1.FileUrl https://xxx.jpg \
    --FileList.1.FileOrderNumber 2
```

Output: 
```
{
    "Response": {
        "RequestId": "e522a812-cb79-1ed4-77ab-908572ghu6qq",
        "TaskId": "209fef6e-117c-11ed-9368-525400e51a47",
        "OperateUrl": "https://ocr.smartform.cloud.tencent.com?taskId=209fef6e-117c-11ed-9368-525400e51a47"
    }
}
```

