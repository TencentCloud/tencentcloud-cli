**Example 1: CreateBatchTask**

离线批处理示例请求

Input: 

```
tccli tione CreateBatchTask --cli-unfold-argument  \
    --BatchTaskName xx \
    --JobType 1 \
    --CronInfo.StartTime 2020-09-22 \
    --CronInfo.EndTime 2020-09-22 \
    --CronInfo.CronConfig xx \
    --ChargeType xx \
    --ResourceGroupId xx \
    --ResourceConfigInfo.Role xx \
    --ResourceConfigInfo.Cpu 1 \
    --ResourceConfigInfo.Memory 1 \
    --ResourceConfigInfo.GpuType xx \
    --ResourceConfigInfo.Gpu 1 \
    --ResourceConfigInfo.InstanceType xx \
    --ResourceConfigInfo.InstanceNum 1 \
    --ResourceConfigInfo.InstanceTypeAlias xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --ModelInfo.ModelId xx \
    --ModelInfo.ModelName xx \
    --ModelInfo.ModelVersionId xx \
    --ModelInfo.ModelVersion xx \
    --ModelInfo.ModelSource xx \
    --ModelInfo.CosPathInfo.Bucket xx \
    --ModelInfo.CosPathInfo.Region xx \
    --ModelInfo.CosPathInfo.Paths xx \
    --ModelInfo.AlgorithmFramework xx \
    --ModelInfo.ModelType xx \
    --ImageInfo.ImageType xx \
    --ImageInfo.ImageUrl xx \
    --ImageInfo.RegistryRegion xx \
    --ImageInfo.RegistryId xx \
    --CodePackage.Bucket xx \
    --CodePackage.Region xx \
    --CodePackage.Paths xx \
    --StartCmd xx \
    --DataConfigs.0.MappingPath xx \
    --DataConfigs.0.DataSourceType xx \
    --DataConfigs.0.DataSetSource.Id xx \
    --DataConfigs.0.COSSource.Bucket xx \
    --DataConfigs.0.COSSource.Region xx \
    --DataConfigs.0.COSSource.Paths xx \
    --DataConfigs.0.CFSSource.Id xx \
    --DataConfigs.0.CFSSource.Path xx \
    --DataConfigs.0.HDFSSource.Id xx \
    --DataConfigs.0.HDFSSource.Path xx \
    --Outputs.0.MappingPath xx \
    --Outputs.0.DataSourceType xx \
    --Outputs.0.DataSetSource.Id xx \
    --Outputs.0.COSSource.Bucket xx \
    --Outputs.0.COSSource.Region xx \
    --Outputs.0.COSSource.Paths xx \
    --Outputs.0.CFSSource.Id xx \
    --Outputs.0.CFSSource.Path xx \
    --Outputs.0.HDFSSource.Id xx \
    --Outputs.0.HDFSSource.Path xx \
    --LogEnable True \
    --LogConfig.LogsetId xx \
    --LogConfig.TopicId xx \
    --VpcId xx \
    --SubnetId xx \
    --Remark xx \
    --CallbackUrl xx
```

Output: 
```
{
    "Response": {
        "BatchTaskId": "xx",
        "RequestId": "xx"
    }
}
```

