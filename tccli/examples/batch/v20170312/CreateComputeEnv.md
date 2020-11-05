**Example 1: Creating a Compute Environment**



Input: 

```
tccli batch CreateComputeEnv --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ComputeEnv.EnvName 'test compute env'\
    --ComputeEnv.EnvDescription 'test compute env'\
    --ComputeEnv.EnvType MANAGED\
    --ComputeEnv.EnvData.InstanceType S1.SMALL2\
    --ComputeEnv.EnvData.ImageId img-bd78fy2t\
    --ComputeEnv.DesiredComputeNodeCount 1
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

