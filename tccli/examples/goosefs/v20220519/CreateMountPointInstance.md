**Example 1: 创建GooseFS MountPoint实例**



Input: 

```
tccli goosefs CreateMountPointInstance --cli-unfold-argument  \
    --ClusterId clst-riQxF21P \
    --MountItems.0.NodeId ins-018x8uuh \
    --MountItems.0.MountPath /mnt/goosefs \
    --MountItems.0.MountSource cos://bucket-1234567890.cos.ap-guangzhou.myqcloud.com/ \
    --MountItems.0.ConfigId cosfs2-config-id-test
```

Output: 
```
{
    "Response": {
        "MountPointIds": [
            "mpc-0fTpu6yK"
        ],
        "RequestId": "b6ee1f2d-1e63-419a-89f3-eb3cd5f12afe"
    }
}
```

