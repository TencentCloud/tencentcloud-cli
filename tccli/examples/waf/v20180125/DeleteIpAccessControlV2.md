**Example 1: 删除IP黑白名单**



Input: 

```
tccli waf DeleteIpAccessControlV2 --cli-unfold-argument  \
    --Domain www.qcloudwaf.com \
    --DeleteAll True \
    --SourceType log \
    --ActionType 1 \
    --RuleIds 55102222 55562222
```

Output: 
```
{
    "Response": {
        "FailedCount": 0,
        "RequestId": "46757c6e-786c-48ca-b5c4-9fa29ece1c9e"
    }
}
```

