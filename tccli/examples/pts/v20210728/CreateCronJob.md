**Example 1: 创建定时任务**

创建定时任务

Input: 

```
tccli pts CreateCronJob --cli-unfold-argument  \
    --ProjectId project-xx \
    --ScenarioId scenario-xx \
    --ScenarioName scenario name \
    --Name cron name \
    --CronExpression */1 * * * * \
    --FrequencyType 1 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --NoticeId notice-xx \
    --JobOwner tom
```

Output: 
```
{
    "Response": {
        "RequestId": "req-xx",
        "CronJobId": "cron-xx"
    }
}
```

