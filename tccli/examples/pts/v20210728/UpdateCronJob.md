**Example 1: 更新定时任务**

更新定时任务

Input: 

```
tccli pts UpdateCronJob --cli-unfold-argument  \
    --ProjectId xx \
    --CronJobId xx \
    --CronExpression */1 * * * * \
    --FrequencyType 1 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --NoticeId xx \
    --Name xx \
    --ScenarioId xx \
    --ScenarioName xx \
    --Note xx \
    --JobOwner xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

