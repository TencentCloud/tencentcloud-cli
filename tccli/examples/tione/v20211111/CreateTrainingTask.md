**Example 1: 创建训练任务**



Input: 

```
tccli tione CreateTrainingTask --cli-unfold-argument  \
    --Remark xx \
    --VpcId xx \
    --Name xx \
    --ImageInfo.ImageUrl xx \
    --ImageInfo.RegistryRegion xx \
    --ImageInfo.RegistryId xx \
    --ImageInfo.ImageType xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --StartCmdInfo.PsStartCmd xx \
    --StartCmdInfo.StartCmd xx \
    --StartCmdInfo.WorkerStartCmd xx \
    --ResourceConfigInfos.0.InstanceType xx \
    --ResourceConfigInfos.0.InstanceNum 1 \
    --ResourceConfigInfos.0.Cpu 1 \
    --ResourceConfigInfos.0.Role xx \
    --ResourceConfigInfos.0.Memory 1 \
    --ResourceConfigInfos.0.Gpu 1 \
    --ResourceConfigInfos.0.GpuType xx \
    --ResourceConfigInfos.0.InstanceTypeAlias xx \
    --CodePackagePath.Paths xx \
    --CodePackagePath.Region xx \
    --CodePackagePath.Bucket xx \
    --TuningParameters xx \
    --ResourceGroupId xx \
    --LogEnable True \
    --FrameworkName xx \
    --DataSource xx \
    --ChargeType xx \
    --SubnetId xx \
    --Output.Paths xx \
    --Output.Region xx \
    --Output.Bucket xx \
    --TrainingMode xx \
    --FrameworkVersion xx \
    --LogConfig.TopicId xx \
    --LogConfig.LogsetId xx \
    --DataConfigs.0.DataSetSource.Id xx \
    --DataConfigs.0.CFSSource.Path xx \
    --DataConfigs.0.CFSSource.Id xx \
    --DataConfigs.0.DataSourceType xx \
    --DataConfigs.0.HDFSSource.Path xx \
    --DataConfigs.0.HDFSSource.Id xx \
    --DataConfigs.0.COSSource.Paths xx \
    --DataConfigs.0.COSSource.Region xx \
    --DataConfigs.0.COSSource.Bucket xx \
    --DataConfigs.0.MappingPath xx
```

Output: 
```
{
    "Response": {
        "Id": "xx",
        "RequestId": "xx"
    }
}
```

