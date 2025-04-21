**Example 1: 示例1**



Input: 

```
tccli ioa ModifyAuthSource --cli-unfold-argument  \
    --Type  \
    --Config  \
    --ExtraConfig  \
    --Name  \
    --Description  \
    --WelcomeTitle  \
    --WelcomeSubtitle  \
    --Id 
```

Output: 
```
{
    "Response": {
        "Data": {
            "UpdateTime": "xx",
            "Name": "xx",
            "Type": "xx",
            "ExtraConfig": "xx",
            "Id": "xx",
            "TypeName": "xx",
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
            "Description": "xx",
            "WelcomeTitle": "xx",
            "Config": "xx",
            "CreateTime": "xx",
            "PresentInfo": [
                {
                    "Value": "xx"
                }
            ],
            "WelcomeSubtitle": "xx"
        },
        "RequestId": "xx"
    }
}
```

