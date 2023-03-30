**Example 1: 设置弹性伸缩配置**

集群配置弹性伸缩策略信息。

Input: 

```
tccli thpc SetAutoScalingConfiguration --cli-unfold-argument  \
    --DryRun false \
    --ShrinkIdleTime 300 \
    --ExpansionBusyTime 120 \
    --ClusterId hpc-5lyv94lq
```

Output: 
```
{
    "Response": {
        "RequestId": "d1d90874-f565-463d-ba1d-c707517eece1"
    }
}
```

