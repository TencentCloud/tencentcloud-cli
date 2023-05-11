**Example 1: 复制作业**



Input: 

```
tccli oceanus CopyJobs --cli-unfold-argument  \
    --WorkSpaceId sapce-xxx \
    --JobItems.0.SourceId cql-pqx9zh30 \
    --JobItems.0.SourceName datagen_datagen_datagen_datagen_datagen_datagen_50 \
    --JobItems.0.JobType 1 \
    --JobItems.0.TargetClusterId cluster-4y035tb0 \
    --JobItems.0.TargetName datagen_datagen_datagen_datagen_datagen_datagen_50_2022-01-12_10_14_52 \
    --JobItems.0.TargetFolderId root
```

Output: 
```
{
    "Response": {
        "CopyJobsResults": [
            {
                "JobId": "cql-pqx9zh30",
                "JobName": "jar3",
                "TargetJobName": "",
                "TargetJobId": "",
                "Message": "Failed to get cluster group",
                "Result": -1,
                "ClusterName": "",
                "ClusterId": ""
            },
            {
                "JobId": "cql-njifzfwn",
                "JobName": "OOM",
                "TargetJobName": "OOM_2021-12-21_17_54_32",
                "TargetJobId": "cql-2dhxz8sf",
                "Message": "OK",
                "Result": 0,
                "ClusterName": "依赖管理二期",
                "ClusterId": "cluster-l0elpxde"
            }
        ],
        "FailCount": 1,
        "RequestId": "123456a",
        "SuccessCount": 1
    }
}
```

