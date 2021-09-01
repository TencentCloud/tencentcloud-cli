**Example 1: 查询训练任务列表**



Input: 

```
tccli tione DescribeTrainingJobs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f7094a2d-ffa8-4dc9-8bd8-2349ea4f9c63",
        "TotalCount": 1,
        "TrainingJobSet": [
            {
                "CreationTime": "2019-11-22 11:09:43",
                "LastModifiedTime": "2019-11-22 11:27:08",
                "TrainingEndTime": null,
                "TrainingJobName": "api_test",
                "TrainingJobStatus": "Failed",
                "ResourceConfig": {
                    "InstanceCount": 1,
                    "InstanceType": "TI.SMALL2.1core2g",
                    "VolumeSizeInGB": 10
                },
                "InstanceId": "timaker-jly3z0hluj"
            }
        ]
    }
}
```

