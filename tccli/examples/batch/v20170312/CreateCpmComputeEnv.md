**Example 1: 创建黑石计算环境**



Input: 

```
tccli batch CreateCpmComputeEnv --cli-unfold-argument  \
    --ComputeEnv.EnvName cpm-env-win \
    --ComputeEnv.EnvData.Zones ap-chongqing-bls-1 \
    --ComputeEnv.EnvData.InstanceTypes PI100v2 \
    --ComputeEnv.EnvData.TimeUnit m \
    --ComputeEnv.EnvData.TimeSpan 1 \
    --ComputeEnv.EnvData.RaidId 3 \
    --ComputeEnv.EnvData.OsTypeId 125 \
    --ComputeEnv.EnvData.VirtualPrivateClouds.0.VpcId vpc-33em4y15 \
    --ComputeEnv.EnvData.VirtualPrivateClouds.0.SubnetId subnet-6x83jiie \
    --ComputeEnv.EnvData.SysRootSpace 100 \
    --ComputeEnv.EnvData.SysDataSpace 50 \
    --ComputeEnv.EnvData.EipPayMode flow \
    --ComputeEnv.EnvData.EipBandwidth 0 \
    --ComputeEnv.EnvData.ApplyEip 0 \
    --ComputeEnv.EnvData.HyperThreading 1 \
    --ComputeEnv.EnvData.AutoRenewFlag 0 \
    --ComputeEnv.DesiredComputeNodeCount 1
```

Output: 
```
{
    "Response": {
        "EnvId": "env-89kunmev",
        "RequestId": "c30340b4-a9a7-4204-98f6-725da4bcc117"
    }
}
```

