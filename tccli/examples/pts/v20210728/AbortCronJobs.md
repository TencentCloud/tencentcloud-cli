**Example 1: 停止定时任务**

停止定时任务

Input: 

```
tccli pts AbortCronJobs --cli-unfold-argument  \
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

