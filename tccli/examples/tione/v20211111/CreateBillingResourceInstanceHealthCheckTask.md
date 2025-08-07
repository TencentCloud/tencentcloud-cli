**Example 1: 创建资源组节点健康检测任务**

创建资源组节点健康检测任务

Input: 

```
tccli tione CreateBillingResourceInstanceHealthCheckTask --cli-unfold-argument  \
    --ResourceGroupId ersg-rf6p8zb8 \
    --ResourceInstanceIds sm-2z84hf49 \
    --SanityCheckConfig.SanityCheckItems.0.Item nccl-test \
    --SanityCheckConfig.SanityCheckTimeoutInMin 2
```

Output: 
```
{
    "Response": {
        "Id": "jkjc-68wtg233",
        "RequestId": "0191f5a9-3f60-4e39-86ab-fb87b225933e"
    }
}
```

