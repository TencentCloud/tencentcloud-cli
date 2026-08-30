**Example 1: 设置队列弹性伸缩配置**

MULTI_CARD + 混合卡数

Input: 

```
tccli thpc SetQueueAutoScaling --cli-unfold-argument  \
    --ClusterId hpc-r7cjxd9c \
    --QueueName as-it-queue \
    --ScalingPolicy.DesiredCapacity 8 \
    --ScalingPolicy.ScalingUnit GPU_CARD \
    --ExpansionPolicy.ExpansionMode MULTI_CARD \
    --ExpansionPolicy.LaunchTemplateIds lt-1dtaw7fw \
    --ExpansionPolicy.TemplateOverrides.InstanceFamilies GN10X \
    --ExpansionPolicy.TemplateOverrides.EnableMixedGpuCount True \
    --ExpansionPolicy.TemplateOverrides.EnableMultiZone True \
    --ExpansionPolicy.ExpansionPriority.InstanceSpecPriority LARGE_FIRST
```

Output: 
```
{
    "Response": {
        "RequestId": "f0fa65b3-2174-4534-87d5-e9434e858b3f"
    }
}
```

