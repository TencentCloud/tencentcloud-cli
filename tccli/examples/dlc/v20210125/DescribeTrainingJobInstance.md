**Example 1: 查看训练实例详情**



Input: 

```
tccli dlc DescribeTrainingJobInstance --cli-unfold-argument  \
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
            "JobRunningTime": 4178486,
            "Priority": 5,
            "SpecId": "raytrain-spec-thjiyg-rbou",
            "SpecName": "cus04",
            "Status": "RUNNING"
        },
        "RequestId": "ad334f05-c755-4404-84b1-b3225d3a8905"
    }
}
```

