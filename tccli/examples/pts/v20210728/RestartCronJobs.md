**Example 1: 重启定时任务**

重启状态为已中止的定时任务

Input: 

```
tccli pts RestartCronJobs --cli-unfold-argument  \
    --ProjectId xx \
    --CronJobIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

