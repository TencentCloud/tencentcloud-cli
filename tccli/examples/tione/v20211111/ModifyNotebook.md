**Example 1: 修改Notebook**

修改Notebook

Input: 

```
tccli tione ModifyNotebook --cli-unfold-argument  \
    --Id abc \
    --Name abc \
    --ChargeType abc \
    --ResourceGroupId abc \
    --ResourceConf.Cpu 1 \
    --ResourceConf.Memory 1 \
    --ResourceConf.Gpu 1 \
    --ResourceConf.GpuType abc \
    --ResourceConf.InstanceType abc \
    --VpcId abc \
    --SubnetId abc \
    --VolumeSizeInGB 1 \
    --VolumeSourceType abc \
    --VolumeSourceCFS.Id abc \
    --VolumeSourceCFS.Path abc \
    --LogEnable True \
    --LogConfig.LogsetId abc \
    --LogConfig.TopicId abc \
    --LifecycleScriptId abc \
    --DefaultCodeRepoId abc \
    --AdditionalCodeRepoIds abc \
    --AutoStopping True \
    --AutomaticStopTime 0 \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --DirectInternetAccess True \
    --RootAccess True \
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
    --DataConfigs.0.CFSTurboSource.Id abc \
    --DataConfigs.0.CFSTurboSource.Path abc \
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
        "RequestId": "abc"
    }
}
```

