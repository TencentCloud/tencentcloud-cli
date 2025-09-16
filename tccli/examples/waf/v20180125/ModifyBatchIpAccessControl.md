**Example 1: 新增批量IP黑白名单**



Input: 

```
tccli waf ModifyBatchIpAccessControl --cli-unfold-argument  \
    --IpList 1.1.1.1 \
    --ActionType 42 \
    --Domains www.testwaf.com www.testwaf2.com \
    --Note  \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 0 \
    --JobDateTime.Timed.0.EndDateTime 0 \
    --JobDateTime.TimeTZone UTC+8 \
    --RuleId 5500894817
```

Output: 
```
{
    "Response": {
        "RequestId": "f03362ba-b50e-4581-88e8-76bdc1b332f5"
    }
}
```

