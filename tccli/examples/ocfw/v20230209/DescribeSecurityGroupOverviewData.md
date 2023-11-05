**Example 1: 企业安全组(新)概览**

企业安全组(新)概览

Input: 

```
tccli ocfw DescribeSecurityGroupOverviewData --cli-unfold-argument  \
    --CurrentAppId 0 \
    --Area abc
```

Output: 
```
{
    "Response": {
        "InRulesCnt": 0,
        "OutRulesCnt": 0,
        "InsCnt": 0,
        "UsedSgCnt": 0,
        "AllSgCnt": 0,
        "SgRulesCnt": 0,
        "EnableRulesCnt": 0,
        "NewRulesCnt": 0,
        "RequestId": "abc"
    }
}
```

