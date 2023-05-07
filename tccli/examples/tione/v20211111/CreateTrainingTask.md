**Example 1: 创建训练任务**

创建训练任务

Input: 

```
tccli tione CreateTrainingTask --cli-unfold-argument  \
    --Name abc \
    --FrameworkName abc \
    --FrameworkVersion abc \
    --FrameworkEnvironment abc \
    --ChargeType abc \
    --ResourceGroupId abc \
    --ResourceConfigInfos.0.Role abc \
    --ResourceConfigInfos.0.Cpu 1 \
    --ResourceConfigInfos.0.Memory 1 \
    --ResourceConfigInfos.0.GpuType abc \
    --ResourceConfigInfos.0.Gpu 1 \
    --ResourceConfigInfos.0.InstanceType abc \
    --ResourceConfigInfos.0.InstanceNum 1 \
    --ResourceConfigInfos.0.InstanceTypeAlias abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --ImageInfo.ImageType abc \
    --ImageInfo.ImageUrl abc \
    --ImageInfo.RegistryRegion abc \
    --ImageInfo.RegistryId abc \
    --CodePackagePath.Bucket abc \
    --CodePackagePath.Region abc \
    --CodePackagePath.Paths abc \
    --StartCmdInfo.StartCmd abc \
    --StartCmdInfo.PsStartCmd abc \
    --StartCmdInfo.WorkerStartCmd abc \
    --TrainingMode abc \
    --DataConfigs.0.MappingPath abc \
    --DataConfigs.0.DataSourceType abc \
    --DataConfigs.0.DataSetSource.Id abc \
    --DataConfigs.0.COSSource.Bucket abc \
    --DataConfigs.0.COSSource.Region abc \
    --DataConfigs.0.COSSource.Paths abc \
    --DataConfigs.0.CFSSource.Id abc \
    --DataConfigs.0.CFSSource.Path abc \
    --DataConfigs.0.HDFSSource.Id abc \
    --DataConfigs.0.HDFSSource.Path abc \
    --VpcId abc \
    --SubnetId abc \
    --Output.Bucket abc \
    --Output.Region abc \
    --Output.Paths abc \
    --LogConfig.LogsetId abc \
    --LogConfig.TopicId abc \
    --TuningParameters abc \
    --LogEnable True \
    --Remark abc \
    --DataSource abc \
    --CallbackUrl abc
```

Output: 
```
{
    "Response": {
        "Id": "abc",
        "RequestId": "abc"
    }
}
```

