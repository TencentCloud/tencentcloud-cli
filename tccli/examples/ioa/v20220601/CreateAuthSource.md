**Example 1: 创建一个同步身份源**

创建一个同步身份源

Input: 

```
tccli ioa CreateAuthSource --cli-unfold-argument  \
    --Name 身份源 \
    --Type WeCom \
    --ExtraConfig {} \
    --Description  \
    --WelcomeTitle {} \
    --Config {} \
    --WelcomeSubtitle {}
```

Output: 
```
{
    "Response": {
        "Data": {
            "UpdateTime": "",
            "Name": "",
            "Type": "",
            "ExtraConfig": "",
            "Id": "",
            "TypeName": "",
            "FactorTypes": [
                {
                    "Name": "",
                    "PrimaryAuthAvailable": true,
                    "Platforms": [
                        ""
                    ],
                    "AdditionalAuthAvailable": true,
                    "ChallengeAuthAvailable": true,
                    "Type": ""
                }
            ],
            "Description": "",
            "WelcomeTitle": "",
            "Config": "",
            "CreateTime": "",
            "PresentInfo": [
                {
                    "Name": "",
                    "Value": ""
                }
            ],
            "WelcomeSubtitle": ""
        },
        "RequestId": ""
    }
}
```

