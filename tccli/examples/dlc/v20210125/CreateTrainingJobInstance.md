**Example 1: 基于训练作业配置创建训练实例**



Input: 

```
tccli dlc CreateTrainingJobInstance --cli-unfold-argument  \
    --SpecId raytrain-spec-thjiyg-rbou
```

Output: 
```
{
    "Response": {
        "Instance": {
            "CheckpointMountInfo": {
                "Bucket": "common-job-packages-251233710",
                "MountPath": "/shared",
                "PlatformManaged": true,
                "Region": "ap-guangzhou",
                "StorageType": "CFS",
                "VolumeSubPath": "/checkpoints/cus04"
            },
            "CreateTime": 1782989786622,
            "Creator": "700002655693",
            "InstanceId": "rayjob-20260702185625-wona",
            "JobCreateTime": 1782989786622,
            "JobRunningTime": 17,
            "Priority": 5,
            "SpecId": "raytrain-spec-thjiyg-rbou",
            "SpecName": "cus04",
            "Status": "SUBMITTED"
        },
        "RequestId": "de80edb4-3d4e-44e4-a0a5-69dab5198717"
    }
}
```

