**Example 1: 更新定时任务**

更新定时任务

Input: 

```
tccli pts UpdateCronJob --cli-unfold-argument  \
    --ProjectId project-xx \
    --CronJobId cron-xx \
    --CronExpression */1 * * * * \
    --FrequencyType 1 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --NoticeId notice-xx \
    --Name cron name \
    --ScenarioId scenario-xx \
    --ScenarioName scenario name \
    --Note notes \
    --JobOwner tom
```

Output: 
```
{
    "Response": {
        "RequestId": "req-xx"
    }
}
```

