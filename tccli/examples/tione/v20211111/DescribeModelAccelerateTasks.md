**Example 1: 查询模型加速任务列表**



Input: 

```
tccli tione DescribeModelAccelerateTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ModelAccelerateTasks": [
            {
                "ModelName": "test-model",
                "ModelAccTaskName": "test-acc-task",
                "ModelAccTaskId": "acc-3wj738qaxy80",
                "ModelVersion": "v1",
                "ModelSource": "COS",
                "Speedup": "2.1x",
                "TaskStatus": "STATUS_SUCCESS",
                "ModelInputPath": {
                    "Paths": [
                        "test/input/inception.pt"
                    ],
                    "Region": "ap-guangzhou",
                    "Bucket": "test-bucket"
                },
                "ChargeType": "FREE",
                "OptimizationLevel": "FP16",
                "GPUType": "T4",
                "ModelOutputPath": {
                    "Paths": [
                        "test/output/"
                    ],
                    "Region": "ap-guangzhou",
                    "Bucket": "test-bucket"
                },
                "ModelId": "m-23014259659902976"
            }
        ],
        "RequestId": "xx"
    }
}
```

