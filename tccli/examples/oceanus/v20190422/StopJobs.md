**Example 1: 批量停止作业示例**



Input: 

```
tccli oceanus StopJobs --cli-unfold-argument  \
    --StopJobDescriptions.0.StopType 0 \
    --StopJobDescriptions.0.JobId cql-glegwraz
```

Output: 
```
{
    "Response": {
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dd08d16"
    }
}
```

