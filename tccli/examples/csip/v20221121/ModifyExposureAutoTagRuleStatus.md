**Example 1: 云边界自动打标规则删除**



Input: 

```
tccli csip ModifyExposureAutoTagRuleStatus --cli-unfold-argument  \
    --RuleID 3 \
    --Enable False \
    --MemberId mem-00000
```

Output: 
```
{
    "Response": {
        "Message": "success",
        "RequestId": "422dc76b-582f-4a3c-8206-00fafaf74183"
    }
}
```

