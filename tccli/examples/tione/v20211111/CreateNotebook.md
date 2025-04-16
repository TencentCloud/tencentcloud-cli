**Example 1: 创建Notebook**

创建Notebook

Input: 

```
tccli tione CreateNotebook --cli-unfold-argument  \
    --Name notebook-test \
    --ChargeType POSTPAID_BY_HOUR \
    --ResourceConf.Cpu 2000 \
    --ResourceConf.Memory 4096 \
    --ResourceConf.Gpu 1 \
    --ResourceConf.GpuType V100 \
    --ResourceConf.InstanceType TI.GN10.2XLARGE40.POST \
    --ResourceGroupId trsg-dwpqnjmk \
    --VpcId vpc-4kq8vlym \
    --SubnetId subnet-58zkmdob \
    --VolumeSourceType CFS \
    --VolumeSizeInGB 1 \
    --VolumeSourceCFS.Id cfs-9su5kqtv \
    --VolumeSourceCFS.Path /tione \
    --LogEnable True \
    --LogConfig.LogsetId 4dd0a097-f629-4afc-9b99-888ef99a178f \
    --LogConfig.TopicId ea8048db-8f97-4abb-9668-f3532b9b61f8 \
    --RootAccess True \
    --LifecycleScriptId ls-1007228485705742720 \
    --DefaultCodeRepoId cr-1000669213287070080 \
    --AdditionalCodeRepoIds cr-1000669213287070081 \
    --AutoStopping True \
    --AutomaticStopTime 1 \
    --Tags.0.TagKey test-key \
    --Tags.0.TagValue test-value \
    --DirectInternetAccess True \
    --DataConfigs.0.MappingPath /home/tione/notebook \
    --DataConfigs.0.DataSourceType CLOUD_PREMIUM \
    --DataConfigs.0.CBSSource.VolumeSizeInGB 50 \
    --ImageInfo.ImageType SYSTEM \
    --ImageInfo.ImageUrl tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v1.8.0 \
    --ImageInfo.ImageName tilearn-llm0.9-torch2.3-py3.10-cuda12.4-gpu \
    --ImageType SYSTEM
```

Output: 
```
{
    "Response": {
        "Id": "nb-1188508294472113920",
        "RequestId": "ecc8d2f6-9772-40df-856f-f6e48c6a7008"
    }
}
```

