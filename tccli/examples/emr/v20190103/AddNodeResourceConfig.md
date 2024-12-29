**Example 1: 增加当前集群的节点规格配置**



Input: 

```
tccli emr AddNodeResourceConfig --cli-unfold-argument  \
    --InstanceId abc \
    --ResourceType abc \
    --IsDefault abc \
    --ResourceConfig.Spec abc \
    --ResourceConfig.StorageType 0 \
    --ResourceConfig.DiskType abc \
    --ResourceConfig.RootSize 0 \
    --ResourceConfig.MemSize 0 \
    --ResourceConfig.Cpu 0 \
    --ResourceConfig.DiskSize 0 \
    --ResourceConfig.MultiDisks.0.DiskType abc \
    --ResourceConfig.MultiDisks.0.Volume 0 \
    --ResourceConfig.MultiDisks.0.Count 0 \
    --ResourceConfig.Tags.0.TagKey abc \
    --ResourceConfig.Tags.0.TagValue abc \
    --ResourceConfig.InstanceType abc \
    --ResourceConfig.LocalDiskNum 1 \
    --ResourceConfig.DiskNum 1 \
    --PayMode 0 \
    --ZoneId 0 \
    --MultipleResourceConfig.0.Spec abc \
    --MultipleResourceConfig.0.StorageType 0 \
    --MultipleResourceConfig.0.DiskType abc \
    --MultipleResourceConfig.0.RootSize 0 \
    --MultipleResourceConfig.0.MemSize 0 \
    --MultipleResourceConfig.0.Cpu 0 \
    --MultipleResourceConfig.0.DiskSize 0 \
    --MultipleResourceConfig.0.MultiDisks.0.DiskType abc \
    --MultipleResourceConfig.0.MultiDisks.0.Volume 0 \
    --MultipleResourceConfig.0.MultiDisks.0.Count 0 \
    --MultipleResourceConfig.0.Tags.0.TagKey abc \
    --MultipleResourceConfig.0.Tags.0.TagValue abc \
    --MultipleResourceConfig.0.InstanceType abc \
    --MultipleResourceConfig.0.LocalDiskNum 1 \
    --MultipleResourceConfig.0.DiskNum 1 \
    --ResourceBaseType abc \
    --ComputeResourceId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "f0f11d21-6d0d-4f73-9177-8ae4ec456068"
    }
}
```

