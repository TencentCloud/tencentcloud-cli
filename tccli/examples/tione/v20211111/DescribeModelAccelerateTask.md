**Example 1: 查询模型优化任务详情**



Input: 

```
tccli tione DescribeModelAccelerateTask --cli-unfold-argument  \
    --ModelAccTaskId acc-783jj121
```

Output: 
```
{
    "Response": {
        "ModelAccRuntimeInSecond": 1,
        "ModelAccStartTime": "xx",
        "ModelAccelerateTask": {
            "ModelName": "xx",
            "ModelAccTaskName": "xx",
            "ModelInputNum": 1,
            "ModelAccTaskId": "xx",
            "ModelVersion": "xx",
            "ModelSource": "xx",
            "Speedup": "xx",
            "TaskStatus": "xx",
            "ModelInputPath": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "ChargeType": "xx",
            "OptimizationLevel": "xx",
            "ModelInputInfos": [
                {
                    "ModelInputDimension": [
                        "xx"
                    ],
                    "ModelInputType": "xx"
                }
            ],
            "GPUType": "xx",
            "ModelOutputPath": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "ModelId": "xx"
        },
        "ModelAccEndTime": "xx",
        "RequestId": "xx"
    }
}
```

