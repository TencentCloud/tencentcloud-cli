**Example 1: DescribeAuthSourceConfigs**



Input: 

```
tccli ioa DescribeAuthSourceConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Switches": {
                        "BuildInSwitch": 0,
                        "EditEnableSwitch": 1,
                        "DeleteEnableSwitch": 1
                    },
                    "FactorTypes": [
                        {
                            "Platforms": [
                                "PC"
                            ],
                            "PrimaryAuthAvailable": true,
                            "AdditionalAuthAvailable": true,
                            "ChallengeAuthAvailable": true,
                            "Name": "扫码认证",
                            "Type": "QRCode"
                        }
                    ],
                    "Id": "jvhc2ffhpqCMbFawZ6wgTh",
                    "WelcomeText": "",
                    "Description": "企业微信",
                    "Name": "企业微信-认证联调",
                    "DBId": 90,
                    "Type": "WeCom"
                },
                {
                    "Switches": {
                        "BuildInSwitch": 1,
                        "EditEnableSwitch": 1,
                        "DeleteEnableSwitch": 0
                    },
                    "FactorTypes": [
                        {
                            "Platforms": [
                                "PC",
                                "Mobile"
                            ],
                            "PrimaryAuthAvailable": true,
                            "AdditionalAuthAvailable": false,
                            "ChallengeAuthAvailable": true,
                            "Name": "账密认证",
                            "Type": "Password"
                        }
                    ],
                    "Id": "iOA",
                    "WelcomeText": "",
                    "Description": "iOA本地账密",
                    "Name": "iOA本地账密",
                    "DBId": 5,
                    "Type": "iOA"
                },
                {
                    "Switches": {
                        "BuildInSwitch": 1,
                        "EditEnableSwitch": 1,
                        "DeleteEnableSwitch": 0
                    },
                    "FactorTypes": [
                        {
                            "Platforms": [
                                "Mobile"
                            ],
                            "PrimaryAuthAvailable": false,
                            "AdditionalAuthAvailable": false,
                            "ChallengeAuthAvailable": true,
                            "Name": "设备认证",
                            "Type": "Device"
                        }
                    ],
                    "Id": "Device",
                    "WelcomeText": "",
                    "Description": "设备认证",
                    "Name": "设备认证",
                    "DBId": 6,
                    "Type": "Device"
                },
                {
                    "Switches": {
                        "BuildInSwitch": 1,
                        "EditEnableSwitch": 1,
                        "DeleteEnableSwitch": 0
                    },
                    "FactorTypes": [
                        {
                            "Platforms": [
                                "PC"
                            ],
                            "PrimaryAuthAvailable": true,
                            "AdditionalAuthAvailable": true,
                            "ChallengeAuthAvailable": true,
                            "Name": "扫码认证",
                            "Type": "QRCode"
                        }
                    ],
                    "Id": "QRCode",
                    "WelcomeText": "",
                    "Description": "扫码认证",
                    "Name": "扫码认证",
                    "DBId": 7,
                    "Type": "QRCode"
                },
                {
                    "Switches": {
                        "BuildInSwitch": 1,
                        "EditEnableSwitch": 1,
                        "DeleteEnableSwitch": 0
                    },
                    "FactorTypes": [
                        {
                            "Platforms": [
                                "PC"
                            ],
                            "PrimaryAuthAvailable": false,
                            "AdditionalAuthAvailable": true,
                            "ChallengeAuthAvailable": true,
                            "Name": "TOTP认证",
                            "Type": "TOTP"
                        }
                    ],
                    "Id": "TOTP",
                    "WelcomeText": "",
                    "Description": "TOTP口令",
                    "Name": "TOTP口令",
                    "DBId": 8,
                    "Type": "TOTP"
                }
            ],
            "Page": {
                "PageNum": 1,
                "PageSize": 5,
                "Total": 5,
                "PageCount": 1
            }
        },
        "RequestId": "570938af-4ebe-4d2b-811d-ffe6e4b7093b"
    }
}
```

