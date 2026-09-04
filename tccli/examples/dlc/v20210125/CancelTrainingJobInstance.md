**Example 1: 暂停（取消）实例**



Input: 

```
tccli dlc CancelTrainingJobInstance --cli-unfold-argument  \
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
            "CreateTime": 1782989786623,
            "Creator": "700002655693",
            "HistoryUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-wdtiljwu/rayjob-20260702185625-wona/",
            "InstanceId": "rayjob-20260702185625-wona",
            "JobCreateTime": 1782989788347,
            "JobRunningTime": 4331589,
            "Priority": 5,
            "SpecId": "raytrain-spec-thjiyg-rbou",
            "SpecName": "cus04",
            "Status": "CANCELLED"
        },
        "RequestId": "5c9e543c-fcb4-4846-b581-40facc8125e1"
    }
}
```

