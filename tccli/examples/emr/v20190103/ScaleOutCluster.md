**Example 1: 集群扩容**



Input: 

```
tccli emr ScaleOutCluster --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --InstanceId emr-m620 \
    --ScaleOutNodeConfig.NodeFlag TASK \
    --ScaleOutNodeConfig.NodeCount 2 \
    --SoftDeployInfo 1 2 \
    --ServiceNodeInfo 7 \
    --YarnNodeLabel CLOUD \
    --EnableStartServiceFlag True \
    --ResourceSpec.SystemDisk.0.DiskType CLOUD_PREMIUM \
    --ResourceSpec.SystemDisk.0.DiskSize 200 \
    --ResourceSpec.SystemDisk.0.Count 1 \
    --ResourceSpec.SystemDisk.0.ExtraPerformance 0 \
    --ResourceSpec.DataDisk.0.DiskType CLOUD_HIGHIO \
    --ResourceSpec.DataDisk.0.DiskSize 4000 \
    --ResourceSpec.DataDisk.0.Count 4 \
    --ResourceSpec.DataDisk.0.ExtraPerformance 0 \
    --ResourceSpec.InstanceType MA5.8XLARGE256
```

Output: 
```
{
    "Response": {
        "ClientToken": "",
        "FlowId": 19239,
        "InstanceId": "emr-m620",
        "RequestId": "11f53a6c-df44-4496-acac-d09b98ccd",
        "TraceId": "1731400002-73146-8002"
    }
}
```

