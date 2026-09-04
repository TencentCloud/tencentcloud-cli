**Example 1: 列出训练作业配置**



Input: 

```
tccli dlc ListTrainingJobSpec --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Catalog": "{\"CFSVolumes\":[{\"FileSystemId\":\"cfs-99dt0xbn\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"checkpoints/cus04\",\"MountPath\":\"/shared\",\"FSId\":null,\"Host\":null,\"PersistVolumeName\":null,\"VpcId\":null,\"SubnetId\":null,\"Uin\":null,\"Region\":null,\"VolumeMountMode\":null,\"Source\":\"checkpoint\",\"AutoCreateSubDir\":true}],\"CFSTurboVolumes\":null,\"COSVolumes\":[{\"Region\":null,\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/checkpoints/cus_multi_mount_05\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/others\",\"PersistVolumeName\":null,\"VolumeMountMode\":null,\"Source\":\"dataset\"}],\"GooseFSVolumes\":null}",
                "CheckpointMountInfo": {
                    "Bucket": "common-job-packages-251233710",
                    "MountPath": "/shared",
                    "PlatformManaged": true,
                    "Region": "ap-guangzhou",
                    "StorageType": "CFS",
                    "VolumeSubPath": "/checkpoints/cus04"
                },
                "CodePackageUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260200065/20260630194144/44a9489e-e60d-4d73-a048-8a5fe39b2d32.zip",
                "CreateTime": 1782976174590,
                "Creator": "700002655693",
                "Description": "cus04 test",
                "Entrypoint": "bash -c 'cd sft_demo && python -m sft_demo.train_local --storage-path /shared'",
                "HasRunningInstances": false,
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab",
                "InstanceCount": 0,
                "Kind": "CUSTOM_CODE",
                "Priority": 5,
                "Queue": "default",
                "ResourceConfig": "{\n  \"Head\": {\n    \"Name\": \"default-head\",\n    \"PodCpu\": 2,\n    \"PodMem\": 8,\n    \"GpuType\": \"\",\n    \"GpuNum\": 0,\n    \"Envs\": [],\n    \"Labels\": [],\n    \"PodNum\": 1,\n    \"HighAvailability\": false\n  },\n  \"Worker\": [\n    {\n      \"Name\": \"default-worker\",\n      \"PodCpu\": 2,\n      \"PodMem\": 8,\n      \"GpuType\": \"\",\n      \"GpuNum\": 0,\n      \"Envs\": [],\n      \"Labels\": [],\n      \"MinPodNum\": 1,\n      \"MaxPodNum\": 1\n    }\n  ]\n}",
                "ResourcePartitionId": "dlc-p-wdtiljwu",
                "RuntimeEnv": "{\n  \"env_vars\": {\n    \"LEARNING_RATE\": \"1e-4\",\n    \"BATCH_SIZE\": \"32\"\n  },\n  \"pip\": []\n}",
                "SpecId": "raytrain-spec-thjd7y-o9ls",
                "SpecName": "cus04",
                "UpdateTime": 1782976174590
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 46,
        "TotalPages": 1,
        "RequestId": "c8925ed5-50af-44a9-bdc4-89a5dfd423db"
    }
}
```

