**Example 1: 创建计算环境**



Input: 

```
tccli batch CreateComputeEnv --cli-unfold-argument  \
    --ComputeEnv.EnvName test compute env \
    --ComputeEnv.EnvDescription EnvDescription \
    --ComputeEnv.EnvType MANAGED \
    --ComputeEnv.EnvData.InstanceType S1.SMALL2 \
    --ComputeEnv.EnvData.ImageId img-bd78fy2t \
    --ComputeEnv.DesiredComputeNodeCount 1 \
    --Placement.Zone ap-guangzhou-2
```

Output: 
```
{
    "Response": {
        "EnvId": "env-3dhmblr3",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

