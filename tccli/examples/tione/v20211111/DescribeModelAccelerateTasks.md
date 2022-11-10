**Example 1: 查询模型加速任务列表**



Input: 

```
tccli tione DescribeModelAccelerateTasks --cli-unfold-argument  \
    --OrderField xx \
    --Limit 1 \
    --Order xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ModelAccelerateTasks": [
            {
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
            }
        ],
        "RequestId": "xx"
    }
}
```

