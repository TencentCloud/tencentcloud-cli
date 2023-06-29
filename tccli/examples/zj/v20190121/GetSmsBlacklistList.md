**Example 1: GetSmsBlacklistList**



Input: 

```
tccli zj GetSmsBlacklistList --cli-unfold-argument  \
    --SignId 451222 \
    --PhoneNum 12312 \
    --Offset 0 \
    --Limit -1 \
    --License xsdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 14,
            "List": {
                "Status": 0,
                "PhoneNum": "xx",
                "SignContent": "xx",
                "SignId": 1,
                "AccountId": 1,
                "ID": 1,
                "CreatedAt": "xx",
                "SmsAccountId": 1
            }
        },
        "RequestId": "xx"
    }
}
```

