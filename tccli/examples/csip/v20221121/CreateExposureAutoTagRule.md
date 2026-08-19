**Example 1: 创建云边界自动打标规则**



Input: 

```
tccli csip CreateExposureAutoTagRule --cli-unfold-argument  \
    --MemberId mem-000000 \
    --RuleName ok2 \
    --Tag legit_business \
    --Description descripton \
    --Enable False \
    --AssetTypes tencent-cvm_instance \
    --Ports 81 \
    --OpenStatuses acl \
    --ApplyNow False
```

Output: 
```
{
    "Response": {
        "RuleID": 5,
        "RequestId": "b1134143-56e4-4b23-8fcf-b3c2b0e6ad71"
    }
}
```

