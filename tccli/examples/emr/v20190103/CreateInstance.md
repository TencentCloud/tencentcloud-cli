**Example 1: 创建实例**



Input: 

```
tccli emr CreateInstance --cli-unfold-argument  \
    --ResourceSpec.MasterResourceSpec.StorageType 5 \
    --ResourceSpec.MasterResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.MasterResourceSpec.Cpu 4 \
    --ResourceSpec.MasterResourceSpec.DiskSize 100 \
    --ResourceSpec.MasterResourceSpec.MemSize 8192 \
    --ResourceSpec.MasterResourceSpec.RootSize 100 \
    --ResourceSpec.MasterResourceSpec.Spec CVM.S2 \
    --ResourceSpec.CoreCount 2 \
    --ResourceSpec.CoreResourceSpec.StorageType 5 \
    --ResourceSpec.CoreResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.CoreResourceSpec.Cpu 4 \
    --ResourceSpec.CoreResourceSpec.DiskSize 100 \
    --ResourceSpec.CoreResourceSpec.MemSize 8192 \
    --ResourceSpec.CoreResourceSpec.RootSize 100 \
    --ResourceSpec.CoreResourceSpec.Spec CVM.S2 \
    --ResourceSpec.MasterCount 1 \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-3 \
    --SupportHA 0 \
    --TimeSpan 3600 \
    --VPCSettings.SubnetId subnet-xxxxxxx \
    --VPCSettings.VpcId vpc-xxxxxx \
    --LoginSettings.Password tencent@cloud123 \
    --PayMode 0 \
    --AutoRenew 0 \
    --TimeUnit s \
    --Software zookeeper-3.4.9 hadoop-2.8.4 knox-1.2.0 \
    --InstanceName emr测试 \
    --ProductId 4
```

Output: 
```
{
    "Response": {
        "RequestId": "d830face-6587-4263-8ab0-56bda265787d",
        "InstanceId": "emr-xxxx"
    }
}
```

