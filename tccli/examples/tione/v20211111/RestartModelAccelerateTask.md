**Example 1: 重启模型加速任务**

重启模型加速任务

Input: 

```
tccli tione RestartModelAccelerateTask --cli-unfold-argument  \
    --ModelName test-model \
    --ModelAccTaskName test-acc-task \
    --ModelAccTaskId acc-3wj738qaxy80 \
    --ModelVersion v1 \
    --ModelSource COS \
    --ModelInputPath.Paths test/input/inception.pt \
    --ModelInputPath.Region ap-guangzhou \
    --ModelInputPath.Bucket test-bucket \
    --ModelOutputPath.Paths test/output/ \
    --ModelOutputPath.Region ap-guangzhou \
    --ModelOutputPath.Bucket test-bucket \
    --ModelFormat TORCH_SCRIPT \
    --TensorInfos input_0:float(1*3*640*640) \
    --OptimizationLevel FP16
```

Output: 
```
{
    "Response": {
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659"
    }
}
```

