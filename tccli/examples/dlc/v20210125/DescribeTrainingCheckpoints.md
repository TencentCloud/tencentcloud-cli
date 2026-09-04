**Example 1: 列出训练实例 Checkpoint 文件列表**



Input: 

```
tccli dlc DescribeTrainingCheckpoints --cli-unfold-argument  \
    --InstanceId rayjob-20260702201005-qv05 \
    --SubPath sft_ray_training/checkpoint_2026-07-02_17-38-33.912702
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "LastModified": 1782984917447,
                "Name": "checkpoint.pt",
                "Path": "sft_ray_training/checkpoint_2026-07-02_17-38-33.912702/checkpoint.pt",
                "Size": 734261,
                "Type": "file"
            }
        ],
        "MountPath": "/shared",
        "SnapshotTimestamp": 1783002347,
        "StoragePath": "/checkpoints/cus04",
        "StorageType": "CFS",
        "SubPath": "sft_ray_training/checkpoint_2026-07-02_17-38-33.912702/",
        "RequestId": "efeae2fd-f3f0-4e55-90a7-da88132259e6"
    }
}
```

