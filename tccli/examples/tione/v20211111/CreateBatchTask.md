**Example 1: CreateBatchTask**



Input: 

```
tccli tione CreateBatchTask --cli-unfold-argument  \
    --Remark xx \
    --VpcId xx \
    --ModelInfo.CosPathInfo.Paths xx \
    --ModelInfo.CosPathInfo.Region xx \
    --ModelInfo.CosPathInfo.Bucket xx \
    --ModelInfo.AlgorithmFramework xx \
    --ModelInfo.ModelVersion xx \
    --ModelInfo.ModelSource xx \
    --ModelInfo.ModelType xx \
    --ModelInfo.ModelName xx \
    --ModelInfo.ModelVersionId xx \
    --ModelInfo.ModelId xx \
    --ImageInfo.ImageUrl xx \
    --ImageInfo.RegistryRegion xx \
    --ImageInfo.RegistryId xx \
    --ImageInfo.ImageType xx \
    --BatchTaskName xx \
    --Outputs.0.DataSourceType xx \
    --Outputs.0.DataSetSource.Id xx \
    --Outputs.0.CFSSource.Path xx \
    --Outputs.0.CFSSource.Id xx \
    --Outputs.0.COSSource.Paths xx \
    --Outputs.0.COSSource.Region xx \
    --Outputs.0.COSSource.Bucket xx \
    --Outputs.0.MappingPath xx \
    --Outputs.0.HDFSSource.Path xx \
    --Outputs.0.HDFSSource.Id xx \
    --StartCmd xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --LogEnable True \
    --ResourceGroupId xx \
    --CodePackage.Paths xx \
    --CodePackage.Region xx \
    --CodePackage.Bucket xx \
    --DataConfigs.0.DataSetSource.Id xx \
    --DataConfigs.0.CFSSource.Path xx \
    --DataConfigs.0.CFSSource.Id xx \
    --DataConfigs.0.DataSourceType xx \
    --DataConfigs.0.HDFSSource.Path xx \
    --DataConfigs.0.HDFSSource.Id xx \
    --DataConfigs.0.COSSource.Paths xx \
    --DataConfigs.0.COSSource.Region xx \
    --DataConfigs.0.COSSource.Bucket xx \
    --DataConfigs.0.MappingPath xx \
    --ChargeType xx \
    --CronInfo.EndTime 2020-09-22 \
    --CronInfo.CronConfig xx \
    --CronInfo.StartTime 2020-09-22 \
    --SubnetId xx \
    --ResourceConfigInfo.InstanceType xx \
    --ResourceConfigInfo.InstanceNum 1 \
    --ResourceConfigInfo.Cpu 1 \
    --ResourceConfigInfo.Role xx \
    --ResourceConfigInfo.Memory 1 \
    --ResourceConfigInfo.Gpu 1 \
    --ResourceConfigInfo.GpuType xx \
    --ResourceConfigInfo.InstanceTypeAlias xx \
    --LogConfig.TopicId xx \
    --LogConfig.LogsetId xx \
    --JobType 1
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

