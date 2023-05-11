**Example 1: 创建环境**

创建环境。

Input: 

```
tccli omics CreateEnvironment --cli-unfold-argument  \
    --Name omics env \
    --Description env description \
    --Config.VPCOption.SubnetZone ap-guangzhou-6 \
    --Config.VPCOption.VPCCIDRBlock 10.8.0.0/16 \
    --Config.VPCOption.SubnetCIDRBlock 10.8.16.0/20 \
    --Config.ClusterOption.Zone ap-guangzhou-6 \
    --Config.ClusterOption.Type KUBERNETES \
    --Config.DatabaseOption.Zone ap-guangzhou-4 \
    --Config.StorageOption.StorageType SD \
    --Config.StorageOption.Zone ap-guangzhou-6 \
    --Config.CVMOption.Zone ap-guangzhou-6 \
    --Config.CVMOption.InstanceType SA3.MEDIUM8
```

Output: 
```
{
    "Response": {
        "RequestId": "946e07f8-f487-46ab-b486-65e362b4a38b",
        "EnvironmentId": "env-lljckw12",
        "WorkflowUuid": "bc5b790b-407e-42c7-b488-a252fee1dcc7"
    }
}
```

