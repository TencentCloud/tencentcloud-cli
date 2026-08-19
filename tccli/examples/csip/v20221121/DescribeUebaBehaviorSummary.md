**Example 1: test**



Input: 

```
tccli csip DescribeUebaBehaviorSummary --cli-unfold-argument  \
    --MemberId mem-e5d75d512c934d2c
```

Output: 
```
{
    "Response": {
        "Data": {
            "AbnormalCount": 7,
            "BehaviorInfo": [
                {
                    "Date": "2024-10-23 11:00:00",
                    "NodeInfo": [
                        {
                            "Key": "AbnormalBehavior",
                            "Name": "异常行为（次）",
                            "Value": "0"
                        },
                        {
                            "Key": "AbnormalUser",
                            "Name": "异常账号（个）",
                            "Value": "0"
                        }
                    ]
                },
                {
                    "Date": "2024-10-23 12:00:00",
                    "NodeInfo": [
                        {
                            "Key": "AbnormalBehavior",
                            "Name": "异常行为（次）",
                            "Value": "0"
                        },
                        {
                            "Key": "AbnormalUser",
                            "Name": "异常账号（个）",
                            "Value": "0"
                        }
                    ]
                },
                {
                    "Date": "2024-10-23 13:00:00",
                    "NodeInfo": [
                        {
                            "Key": "AbnormalBehavior",
                            "Name": "异常行为（次）",
                            "Value": "0"
                        },
                        {
                            "Key": "AbnormalUser",
                            "Name": "异常账号（个）",
                            "Value": "0"
                        }
                    ]
                }
            ],
            "IsAccess": true
        },
        "RequestId": "abc"
    }
}
```

