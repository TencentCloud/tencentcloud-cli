**Example 1: 批量创建 TWeSee 语义理解任务 - 成功**



Input: 

```
tccli iotexplorer BatchCreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --Inputs.0.ProductId 4AHMY9X89Y \
    --Inputs.0.DeviceName dev002 \
    --Inputs.0.InputURL https://example.qq.com/video.mp4
```

Output: 
```
{
    "Response": {
        "Outputs": [
            {
                "Created": true,
                "TaskId": "019a0fb5-f039-740f-9e5f-1b01fce8a7da"
            }
        ],
        "RequestId": "a1a9472e-4d48-4494-bfa5-c0b744173452"
    }
}
```

**Example 2: 批量创建 TWeSee 语义理解任务 - 失败**



Input: 

```
tccli iotexplorer BatchCreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --Inputs.0.ProductId 4AHMY9X89Y \
    --Inputs.0.DeviceName dev002 \
    --Inputs.0.InputURL https://example.qq.com/video.mp4
```

Output: 
```
{
    "Response": {
        "Outputs": [
            {
                "Created": false,
                "ErrorCode": "InvalidParameter",
                "ErrorMessage": "参数错误:InputURL"
            }
        ],
        "RequestId": "feb44033-42f2-4bb3-bb7a-ffa1fcec95d2"
    }
}
```

