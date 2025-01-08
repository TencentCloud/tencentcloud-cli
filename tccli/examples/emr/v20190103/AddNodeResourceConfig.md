**Example 1: 增加当前集群的节点规格配置**



Input: 

```
tccli emr AddNodeResourceConfig --cli-unfold-argument  \
    --HardwareResourceType HOST \
    --InstanceId emr-llp6c58v \
    --PayMode 0 \
    --ResourceConfig.Cpu 4 \
    --ResourceConfig.DiskSize 0 \
    --ResourceConfig.DiskType CLOULD_SSD \
    --ResourceConfig.InstanceType SA5.LARGE16 \
    --ResourceConfig.MemSize 16384 \
    --ResourceConfig.Spec SA5 \
    --ResourceConfig.StorageType 0 \
    --ResourceType TASK \
    --ZoneId 100007
```

Output: 
```
{
    "Response": {
        "RequestId": "f0f11d21-6d0d-4f73-9177-8ae4ec456068"
    }
}
```

