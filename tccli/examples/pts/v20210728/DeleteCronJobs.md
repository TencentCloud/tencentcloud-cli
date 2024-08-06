**Example 1: 删除定时任务**

删除定时任务

Input: 

```
tccli pts DeleteCronJobs --cli-unfold-argument  \
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

