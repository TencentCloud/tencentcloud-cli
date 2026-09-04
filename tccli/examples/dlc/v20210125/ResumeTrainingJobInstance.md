**Example 1: 断点续训（克隆实例）**



Input: 

```
tccli dlc ResumeTrainingJobInstance --cli-unfold-argument  \
    --InstanceId rayjob-20260702185625-wona
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
            "CreateTime": 1782994206461,
            "Creator": "700002655693",
            "InstanceId": "rayjob-20260702201005-qv05",
            "JobCreateTime": 1782994206461,
            "JobRunningTime": 15,
            "SpecId": "raytrain-spec-thjiyg-rbou",
            "SpecName": "cus04",
            "Status": "SUBMITTED"
        },
        "RequestId": "942f175a-b297-4708-ae81-2f4e7d1f305e"
    }
}
```

