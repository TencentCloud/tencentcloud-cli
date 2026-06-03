**Example 1: 编辑批量精装白名单规则**



Input: 

```
tccli waf ModifyBatchCustomWhiteRule --cli-unfold-argument  \
    --ID 1101 \
    --Name name \
    --SortId 100 \
    --Domains waf.tencentcloudapi.com \
    --Bypass cc acl \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 1711618518 \
    --JobDateTime.Timed.0.EndDateTime 1711918518 \
    --JobDateTime.TimeTZone UTC+8 \
    --Strategies.0.Field COOKIE \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content cookie_value \
    --Strategies.0.Arg cookie_key
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8"
    }
}
```

