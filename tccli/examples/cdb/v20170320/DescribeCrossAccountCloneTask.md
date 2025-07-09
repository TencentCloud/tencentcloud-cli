**Example 1: 查询跨账号克隆信息**

查询跨账号克隆详细信息，包括任务状态、进度信息、错误信息等

Input: 

```
tccli cdb DescribeCrossAccountCloneTask --cli-unfold-argument  \
    --JobId 256117ed-efa08b54-61784d44-91781bbd
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "ErrMsg": "没有错误信息",
        "Status": "success",
        "ProcessInfo": {
            "AllStepsCount": 5,
            "NowStepIndex": 1,
            "AllStepsDesc": [
                {
                    "Progress": 100,
                    "StepDesc": "实例初始化中",
                    "StepEndTime": "2025-05-22 17:27:58",
                    "StepStartTime": "2025-05-22 17:24:24"
                }
            ],
            "SrcInstanceId": "cdb-je5cfmdl",
            "DstInstanceId": "cdb-d3dft2kn",
            "StartTime": "2025-05-22 17:24:11",
            "EndTime": "2025-05-22 17:34:18"
        }
    }
}
```

