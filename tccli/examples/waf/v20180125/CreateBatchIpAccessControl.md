**Example 1: 新增批量IP黑白名单**



Input: 

```
tccli waf CreateBatchIpAccessControl --cli-unfold-argument  \
    --IpList 12.32.4.3 \
    --ActionType 42 \
    --Domains www.testwaf.com www.testwaf2.com \
    --Note  \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 0 \
    --JobDateTime.Timed.0.EndDateTime 0 \
    --JobDateTime.TimeTZone UTC+8
```

Output: 
```
{
    "Response": {
        "RequestId": "5331fe64-a3a5-49c4-8c4b-ada147d91403",
        "RuleId": 5500921210
    }
}
```

