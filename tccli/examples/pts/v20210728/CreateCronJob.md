**Example 1: 创建定时任务**

创建定时任务

Input: 

```
tccli pts CreateCronJob --cli-unfold-argument  \
    --ProjectId xx \
    --ScenarioId xx \
    --ScenarioName xx \
    --Name xx \
    --CronExpression */1 * * * * \
    --FrequencyType 1 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --NoticeId xx \
    --JobOwner tom
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "CronJobId": "cron-xx"
    }
}
```

