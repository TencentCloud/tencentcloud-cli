**Example 1: 创建实例**



Input: 

```
tccli emr CreateInstance --cli-unfold-argument  \
    --ProductId 4 \
    --SupportHA 0 \
    --InstanceName emr测试 \
    --PayMode 0 \
    --Placement.Zone ap-guangzhou-3 \
    --Placement.ProjectId 0 \
    --AutoRenew 0 \
    --Software hadoop-2.8.4 zookeeper-3.4.9 knox-1.2.0 \
    --ResourceSpec.MasterResourceSpec.MemSize 8192 \
    --ResourceSpec.MasterResourceSpec.Cpu 4 \
    --ResourceSpec.MasterResourceSpec.DiskSize 100 \
    --ResourceSpec.MasterResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.MasterResourceSpec.Spec CVM.S2 \
    --ResourceSpec.MasterResourceSpec.RootSize 100 \
    --ResourceSpec.MasterResourceSpec.StorageType 5 \
    --ResourceSpec.CoreResourceSpec.MemSize 8192 \
    --ResourceSpec.CoreResourceSpec.Cpu 4 \
    --ResourceSpec.CoreResourceSpec.DiskSize 100 \
    --ResourceSpec.CoreResourceSpec.DiskType CLOUD_PREMIUM \
    --ResourceSpec.CoreResourceSpec.Spec CVM.S2 \
    --ResourceSpec.CoreResourceSpec.RootSize 100 \
    --ResourceSpec.CoreResourceSpec.StorageType 5 \
    --ResourceSpec.MasterCount 1 \
    --ResourceSpec.CoreCount 2 \
    --VPCSettings.VpcId vpc-xxxxxx \
    --VPCSettings.SubnetId subnet-xxxxxxx \
    --LoginSettings.Password tencent@cloud123 \
    --TimeSpan 3600 \
    --TimeUnit s
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

