**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAuthSourceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthSourceTypeSet": [
                {
                    "FactorTypes": [
                        {
                            "Name": "xx",
                            "PrimaryAuthAvailable": true,
                            "Platforms": [
                                "xx"
                            ],
                            "AdditionalAuthAvailable": true,
                            "ChallengeAuthAvailable": true,
                            "Type": "xx"
                        }
                    ],
                    "Type": "xx",
                    "Name": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

