**Example 1: 创建训练任务**

创建训练任务

Input: 

```
tccli tione CreateTrainingTask --cli-unfold-argument  \
    --Name zhangsan-lora \
    --FrameworkName PYTORCH \
    --FrameworkEnvironment tilearn-llm1.0-torch2.1-angel-vllm1.0-py3.10-cuda12.1-gpu \
    --TrainingMode DDP \
    --ChargeType PREPAID \
    --ResourceConfigInfos.0.Role WORKER \
    --ResourceConfigInfos.0.Cpu 1000 \
    --ResourceConfigInfos.0.Memory 1024 \
    --ResourceConfigInfos.0.GpuType  \
    --ResourceConfigInfos.0.Gpu 0 \
    --ResourceConfigInfos.0.InstanceType  \
    --ResourceConfigInfos.0.InstanceTypeAlias  \
    --ResourceConfigInfos.0.InstanceNum 1 \
    --ResourceGroupId ersg-rf6p8zb8 \
    --Remark  \
    --CodePackagePath.Bucket test-gz-1256580188 \
    --CodePackagePath.Region ap-guangzhou \
    --CodePackagePath.Paths test/ \
    --EncodedStartCmdInfo.StartCmdInfo eyJTdGFydENtZCI6IiIsIlBzU3RhcnRDbWQiOiIiLCJXb3JrZXJTdGFydENtZCI6InNsZWVwIDEwIn0= \
    --DataConfigs.0.DataSourceType CFS \
    --DataConfigs.0.MappingPath /opt/ml/input/data/ \
    --DataConfigs.0.CFSSource.Id cfs-pchxhlg9 \
    --DataConfigs.0.CFSSource.Path /bin \
    --TuningParameters {"test":"test"} \
    --Output.Bucket test-gz-1256580188 \
    --Output.Region ap-guangzhou \
    --Output.Paths cos_test/ \
    --LogEnable False \
    --VpcId vpc-a26qv3af \
    --SubnetId subnet-m7xhqcyc
```

Output: 
```
{
    "Response": {
        "Id": "train-1208038387393233920",
        "RequestId": "0161f5a9-3f60-4e39-86ab-fb87b225964d"
    }
}
```

