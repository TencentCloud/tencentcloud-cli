**Example 1: 更新时间模板**



Input: 

```
tccli iotvideoindustry UpdateTimeTemplate --cli-unfold-argument  \
    --IsAllWeek 0 \
    --TimeTemplateSpecs.0.DayofWeek 0 \
    --TimeTemplateSpecs.0.EndTime xx \
    --TimeTemplateSpecs.0.BeginTime xx \
    --Name xx \
    --TemplateId xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "e1b9e7ac-0989-4af9-a454-26f69d6997d9",
        "Status": "OK"
    }
}
```

