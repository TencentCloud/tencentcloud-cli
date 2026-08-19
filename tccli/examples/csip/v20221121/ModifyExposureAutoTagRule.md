**Example 1: 云边界自动打标规则更新**



Input: 

```
tccli csip ModifyExposureAutoTagRule --cli-unfold-argument  \
    --RuleName rule_name \
    --Tag legit_business \
    --RuleID 3 \
    --MemberId mem-900000 \
    --Description tessssss \
    --AssetTypes tencent-clb_instance \
    --Ports 80 \
    --OpenStatuses open
```

Output: 
```
{
    "Response": {
        "Message": "success",
        "RequestId": "fd07cc32-466a-4f92-b63a-a57b43709638"
    }
}
```

