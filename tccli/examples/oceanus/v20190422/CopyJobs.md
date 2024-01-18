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
        "SuccessCount": 0,
        "FailCount": 0,
        "CopyJobsResults": [
            {
                "JobId": "abc",
                "JobName": "abc",
                "TargetJobName": "abc",
                "TargetJobId": "abc",
                "Message": "abc",
                "Result": 0,
                "ClusterName": "abc",
                "ClusterId": "abc",
                "JobType": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

