**Example 1: 停止定时任务**

停止定时任务

Input: 

```
tccli pts AbortCronJobs --cli-unfold-argument  \
    --ProjectId project-xx \
    --CronJobIds cron-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "req-xx"
    }
}
```

