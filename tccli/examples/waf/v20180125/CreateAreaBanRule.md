**Example 1: 添加地域封禁规则**



Input: 

```
tccli waf CreateAreaBanRule --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Areas.0.Country 中国 \
    --Areas.0.Region 广东 \
    --Areas.0.City 深圳 \
    --JobType CronJob \
    --JobDateTime.Timed.0.StartDateTime 1711618518 \
    --JobDateTime.Timed.0.EndDateTime 1711918518 \
    --JobDateTime.Cron.0.WDays 2 \
    --JobDateTime.Cron.0.StartTime 12:11 \
    --JobDateTime.Cron.0.EndTime 21:00 \
    --JobDateTime.TimeTZone UTC+8 \
    --Lang cn
```

Output: 
```
{
    "Response": {
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

