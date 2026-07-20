**Example 1: 处置封禁**



Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleDirection 1 \
    --HandleTime 7 \
    --HandleComment  \
    --HandleType 1 \
    --AlertDirection 0 \
    --HandleEventIdList f7005f0846e155df126c13636c845388
```

Output: 
```
{
    "Response": {
        "RequestId": "eaf4f272-c04c-49b8-8456-58ff21226bac",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

