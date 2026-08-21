**Example 1: 设置其他配置**

设置其他配置

Input: 

```
tccli csip ModifyBaselineUserOtherConf --cli-unfold-argument  \
    --UserConf.AllowSync True \
    --UserConf.CleanRiskWhenOffline True \
    --UserConf.AgentScanTimeout 1800 \
    --MemberId mem-************95752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "86233d52-d6b6-4615-81e8-69d1e56a1617"
    }
}
```

