**Example 1: 批量同步执行 TWeSee 语义理解任务 - 成功**



Input: 

```
tccli iotexplorer BatchInvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
                "Completed": true,
                "Result": {
                    "DetectedClassifications": [
                        "person"
                    ],
                    "Status": 3,
                    "Summary": "穿白衣服的人在雨后路边行走"
                },
                "TaskId": "019a0bdb-1471-77c7-ad24-3962edda28cc"
            }
        ],
        "RequestId": "79d19408-d4e8-467a-8e93-b6e164d1cb6f"
    }
}
```

**Example 2: 批量同步执行 TWeSee 语义理解任务 - 失败**



Input: 

```
tccli iotexplorer BatchInvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
                "Completed": false,
                "ErrorCode": "InvalidParameter",
                "ErrorMessage": "参数错误:InputURL"
            }
        ],
        "RequestId": "fa6f4dfb-45eb-4263-b889-e46b50bfcdbf"
    }
}
```

