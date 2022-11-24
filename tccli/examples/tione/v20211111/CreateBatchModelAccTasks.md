**Example 1: 批量创建模型加速任务**



Input: 

```
tccli tione CreateBatchModelAccTasks --cli-unfold-argument  \
    --BatchModelAccTasks.0.ModelName test \
    --BatchModelAccTasks.0.ModelFormat TORCH_SCRIPT \
    --BatchModelAccTasks.0.ModelVersion v1 \
    --BatchModelAccTasks.0.ModelSource COS \
    --BatchModelAccTasks.0.ModelInputPath.Paths test/input/inception.pt \
    --BatchModelAccTasks.0.ModelInputPath.Region ap-guangzhou \
    --BatchModelAccTasks.0.ModelInputPath.Bucket test-bucket \
    --BatchModelAccTasks.0.AccEngineVersion v2.0 \
    --BatchModelAccTasks.0.TensorInfos input_0:float(1*3*640*640) \
    --BatchModelAccTasks.0.ModelId m-660879334503305216 \
    --ModelAccTaskName test-acc-task \
    --ModelOutputPath.Paths test/output/ \
    --ModelOutputPath.Region ap-guangzhou \
    --ModelOutputPath.Bucket test-bucket \
    --Tags.0.TagKey test-key \
    --Tags.0.TagValue test-value \
    --HyperParameter.CpuCachePercentage 0.2 \
    --HyperParameter.SlotNum 1 \
    --HyperParameter.GpuCachePercentage 0.2 \
    --HyperParameter.MaxNNZ 1 \
    --OptimizationLevel FP16 \
    --GPUType T4
```

Output: 
```
{
    "Response": {
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659",
        "ModelAccTaskIds": [
            "acc-50rjzj2xtest"
        ]
    }
}
```

