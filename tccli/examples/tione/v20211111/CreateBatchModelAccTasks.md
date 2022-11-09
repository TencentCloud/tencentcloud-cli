**Example 1: 批量创建模型加速任务**



Input: 

```
tccli tione CreateBatchModelAccTasks --cli-unfold-argument  \
    --BatchModelAccTasks.0.ModelName xx \
    --BatchModelAccTasks.0.ModelFormat xx \
    --BatchModelAccTasks.0.ModelVersion xx \
    --BatchModelAccTasks.0.ModelSource xx \
    --BatchModelAccTasks.0.ModelInputPath.Paths xx \
    --BatchModelAccTasks.0.ModelInputPath.Region xx \
    --BatchModelAccTasks.0.ModelInputPath.Bucket xx \
    --BatchModelAccTasks.0.AccEngineVersion xx \
    --BatchModelAccTasks.0.TensorInfos xx \
    --BatchModelAccTasks.0.ModelId xx \
    --ModelAccTaskName xx \
    --ModelOutputPath.Paths xx \
    --ModelOutputPath.Region xx \
    --ModelOutputPath.Bucket xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --HyperParameter.EnableDistributed xx \
    --HyperParameter.CpuCachePercentage xx \
    --HyperParameter.SlotNum xx \
    --HyperParameter.GpuCachePercentage xx \
    --HyperParameter.MaxNNZ xx \
    --OptimizationLevel xx \
    --GPUType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ModelAccTaskIds": [
            "xx"
        ]
    }
}
```

