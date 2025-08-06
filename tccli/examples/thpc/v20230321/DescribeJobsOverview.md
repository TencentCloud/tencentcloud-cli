**Example 1: thpc查看集群下的作业概览信息**

thpc查看集群下的作业概览信息

Input: 

```
tccli thpc DescribeJobsOverview --cli-unfold-argument  \
    --ClusterId hpc-xxx
```

Output: 
```
{
    "Response": {
        "JobTotal": 3,
        "QueuingJobTotal": 2,
        "RunningJobTotal": 1,
        "RequestId": "a0a8bfa0-43cd-424e-9b12-eb01fadfadc6c1"
    }
}
```

