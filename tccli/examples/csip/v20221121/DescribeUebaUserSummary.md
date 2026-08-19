**Example 1: test**



Input: 

```
tccli csip DescribeUebaUserSummary --cli-unfold-argument  \
    --MemberId mem-5b2c2010c18f07a
```

Output: 
```
{
    "Response": {
        "Data": {
            "AbnormalUserCount": 0,
            "AllUserCount": 13,
            "CustomUserCount": 1,
            "Element": [
                {
                    "Count": 1,
                    "LogType": "1_4",
                    "MemberID": "mem-625c522c0913c901",
                    "UserID": "appid"
                }
            ],
            "SubUserCount": 11,
            "UserCount": 12
        },
        "RequestId": "9d4d4cf6-c76f-4e35-beae-30160e85e7ee"
    }
}
```

