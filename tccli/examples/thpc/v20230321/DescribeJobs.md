**Example 1: 查询指定作业ID的任务列表信息**

查询指定作业ID的任务列表信息

Input: 

```
tccli thpc DescribeJobs --cli-unfold-argument  \
    --JobIds job-mudo8mj
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "ClusterId": "hpc-59wddafa",
                "CreateTime": "2024-12-17 15:31:14",
                "EndTime": "1753-01-01 00:00:00",
                "JobDescription": "job test",
                "JobId": "job-mudo8mij",
                "JobName": "nj-test",
                "JobState": "RUNNING",
                "Priority": 1,
                "QueueName": "compute"
            }
        ],
        "RequestId": "a0a8bfa0-43cd-424e-9b12-eb01fadfadc6c1",
        "TotalCount": 1
    }
}
```

