**Example 1: 重启模型加速任务**



Input: 

```
tccli tione RestartModelAccelerateTask --cli-unfold-argument  \
    --ModelName xx \
    --ModelAccTaskName xx \
    --ModelAccTaskId xx \
    --ModelVersion xx \
    --ModelSource xx \
    --ModelInputPath.Paths xx \
    --ModelInputPath.Region xx \
    --ModelInputPath.Bucket xx \
    --ModelOutputPath.Paths xx \
    --ModelOutputPath.Region xx \
    --ModelOutputPath.Bucket xx \
    --ModelFormat xx \
    --TensorInfos xx \
    --OptimizationLevel xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

