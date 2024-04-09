**Example 1: CreateBatchTask**

批量预测示例请求

Input: 

```
tccli tione CreateBatchTask --cli-unfold-argument  \
    --BatchTaskName task-xx \
    --ChargeType POSTPAID_BY_HOUR \
    --ResourceGroupId trsg-c7xxxx \
    --ResourceConfigInfo.Role WORKER \
    --ResourceConfigInfo.Cpu 1 \
    --ResourceConfigInfo.Memory 1 \
    --ResourceConfigInfo.GpuType A \
    --ResourceConfigInfo.Gpu 1 \
    --ResourceConfigInfo.InstanceType TI.S.LARGE.POST-XXX \
    --ResourceConfigInfo.InstanceNum 1 \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue def \
    --ModelInfo.ModelId abc-id \
    --ModelInfo.ModelName Pytorch \
    --ModelInfo.ModelVersionId mv-v2-abcdef \
    --ModelInfo.ModelVersion v2 \
    --ModelInfo.ModelSource cos \
    --ModelInfo.CosPathInfo.Bucket test-sh-123 \
    --ModelInfo.CosPathInfo.Region ap-shanghai \
    --ModelInfo.CosPathInfo.Paths test/model \
    --ModelInfo.AlgorithmFramework torch \
    --ModelInfo.ModelType ACCELERATE \
    --ImageInfo.ImageType CCR \
    --ImageInfo.ImageUrl ccr.tencentyun.com/a/b/c \
    --ImageInfo.RegistryRegion  \
    --ImageInfo.RegistryId  \
    --CodePackage.Bucket testbkt-1234 \
    --CodePackage.Region ap-shanghai \
    --CodePackage.Paths test/model/code_Path \
    --StartCmd python3 /opt/ml/code/model_service.py \
    --StartCmdBase64 L2FwcC9ydW4uc2g= \
    --DataConfigs.0.MappingPath  \
    --DataConfigs.0.DataSourceType  \
    --DataConfigs.0.DataSetSource.Id 12345678 \
    --DataConfigs.0.COSSource.Bucket test-bkt-1234 \
    --DataConfigs.0.COSSource.Region ap-shanghai \
    --DataConfigs.0.COSSource.Paths test/data/ \
    --DataConfigs.0.CFSSource.Id 12345 \
    --DataConfigs.0.CFSSource.Path /data \
    --DataConfigs.0.HDFSSource.Id 12345 \
    --DataConfigs.0.HDFSSource.Path test/hdfs_path/ \
    --Outputs.0.MappingPath  \
    --Outputs.0.DataSourceType cos \
    --Outputs.0.DataSetSource.Id ds-12345-xx \
    --Outputs.0.COSSource.Bucket testbkt-12345 \
    --Outputs.0.COSSource.Region ap-shanghai \
    --Outputs.0.COSSource.Paths tests/outputs/ \
    --Outputs.0.CFSSource.Id  \
    --Outputs.0.CFSSource.Path  \
    --Outputs.0.HDFSSource.Id  \
    --Outputs.0.HDFSSource.Path  \
    --LogEnable True \
    --LogConfig.LogsetId 123456 \
    --LogConfig.TopicId topic-12345 \
    --VpcId 12345 \
    --SubnetId 12345 \
    --Remark  \
    --CallbackUrl 
```

Output: 
```
{
    "Response": {
        "BatchTaskId": "task-123-xx",
        "RequestId": "abcdef-1234"
    }
}
```

