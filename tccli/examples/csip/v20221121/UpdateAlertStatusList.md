**Example 1: test**



Input: 

```
tccli csip UpdateAlertStatusList --cli-unfold-argument  \
    --OperatedMemberId abc \
    --ID.0.AppId abc \
    --ID.0.Type abc \
    --ID.0.SubType abc \
    --ID.0.Source abc \
    --ID.0.Name abc \
    --ID.0.Key abc \
    --ID.0.Date abc \
    --ID.0.Status 0 \
    --OperateType 0
```

Output: 
```
{
    "Response": {
        "Msg": "abc",
        "Code": "abc",
        "RequestId": "abc"
    }
}
```

