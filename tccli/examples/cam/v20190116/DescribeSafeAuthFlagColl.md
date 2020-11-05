**Example 1: Querying security settings**



Input: 

```
tccli cam DescribeSafeAuthFlagColl --cli-unfold-argument  \
    --SubUin 1234567
```

Output: 
```
{
    "Response": {
        "LoginFlag": {
            "Phone": 1,
            "Token": 0,
            "Stoken": 0,
            "Wechat": 0,
            "Custom": 0
        },
        "ActionFlag": {
            "Phone": 0,
            "Token": 0,
            "Stoken": 0,
            "Wechat": 0,
            "Custom": 0
        },
        "OffsiteFlag": {
            "VerifyFlag": 0,
            "NotifyPhone": 1,
            "NotifyEmail": 1,
            "NotifyWechat": 1,
            "Tips": 0
        },
        "RequestId": "9626da03-4645-4c54-ba90-74836284af0c"
    }
}
```

