**Example 1: 创建Notebook**

创建Notebook

Input: 

```
tccli tione CreateNotebook --cli-unfold-argument  \
    --Name abc \
    --ChargeType abc \
    --ResourceConf.Cpu 1 \
    --ResourceConf.Memory 1 \
    --ResourceConf.Gpu 1 \
    --ResourceConf.GpuType abc \
    --ResourceConf.InstanceType abc \
    --ResourceGroupId abc \
    --VpcId abc \
    --SubnetId abc \
    --VolumeSourceType abc \
    --VolumeSizeInGB 1 \
    --VolumeSourceCFS.Id abc \
    --VolumeSourceCFS.Path abc \
    --LogEnable True \
    --LogConfig.LogsetId abc \
    --LogConfig.TopicId abc \
    --RootAccess True \
    --LifecycleScriptId abc \
    --DefaultCodeRepoId abc \
    --AdditionalCodeRepoIds abc \
    --AutoStopping True \
    --AutomaticStopTime 1 \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --DirectInternetAccess True \
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
    --DataConfigs.0.GooseFSSource.Id abc \
    --ImageInfo.ImageType abc \
    --ImageInfo.ImageUrl abc \
    --ImageInfo.RegistryRegion abc \
    --ImageInfo.RegistryId abc \
    --ImageType abc
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

