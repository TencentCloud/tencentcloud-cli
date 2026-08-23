**Example 1: 批量修改告警状态**



Input: 

```
tccli csip ModifySkillScanAlertStatus --cli-unfold-argument  \
    --IDs 10001 10002 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "SuccessCount": 2,
        "RequestId": "7d7bf0da-5893-4588-90ff-bdc1cc3ea19a"
    }
}
```

