**Example 1: 查询训练任务**



Input: 

```
tccli tione DescribeTrainingJob --cli-unfold-argument  \
    --TrainingJobName api_test
```

Output: 
```
{
    "Response": {
        "RequestId": "9f91ba5c-03bb-4c02-b9cc-d2740821112f",
        "TrainingJobName": "api_test",
        "AlgorithmSpecification": {
            "AlgorithmName": null,
            "TrainingImageName": "ccr.ccs.tencentyun.com/ti_public/tensorflow:1.14.0-py3",
            "TrainingInputMode": "File"
        },
        "HyperParameters": "{\"b\":2}",
        "InputDataConfig": [
            {
                "ChannelName": "training",
                "ContentType": null,
                "DataSource": null,
                "InputMode": null
            }
        ],
        "OutputDataConfig": {
            "CosOutputBucket": "ti-ap-guangzhou-100005457260-1256633383",
            "CosOutputKeyPrefix": ""
        },
        "StoppingCondition": {
            "MaxRuntimeInSeconds": 86400
        },
        "ResourceConfig": {
            "InstanceCount": 1,
            "InstanceType": "TI.SMALL2.1core2g",
            "VolumeSizeInGB": 10
        },
        "VpcConfig": null,
        "RoleName": "role_name",
        "FailureReason": "create training job failure",
        "LastModifiedTime": "2019-11-22 11:57:52",
        "TrainingStartTime": null,
        "TrainingEndTime": null,
        "ModelArtifacts": null,
        "TrainingJobStatus": "Failed",
        "SecondaryStatus": "Failed",
        "SecondaryStatusTransitions": [
            {
                "StartTime": "2019-11-22 11:09:52",
                "EndTime": "2019-11-22 11:11:34",
                "Status": "Starting",
                "StatusMessage": "Launching ML instance"
            },
            {
                "StartTime": "2019-11-22 11:11:34",
                "EndTime": "2019-11-22 11:11:36",
                "Status": "Starting",
                "StatusMessage": "ML instance ready"
            },
            {
                "StartTime": "2019-11-22 11:11:36",
                "EndTime": "2019-11-22 11:11:37",
                "Status": "Downloading",
                "StatusMessage": "Training data ready"
            },
            {
                "StartTime": "2019-11-22 11:11:37",
                "EndTime": null,
                "Status": "Failed",
                "StatusMessage": "create training job failure"
            }
        ]
    }
}
```

