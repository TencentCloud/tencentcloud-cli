**Example 1: DescribeRulesSetting**



Input: 

```
tccli teo DescribeRulesSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4",
        "Actions": [
            {
                "Action": "ErrorPage",
                "Properties": [
                    {
                        "ChoiceProperties": [],
                        "ChoicesValue": [],
                        "ExtraParameter": {
                            "Choices": [
                                "403",
                                "404",
                                "404",
                                "405",
                                "414",
                                "416",
                                "451",
                                "500",
                                "501",
                                "502",
                                "503",
                                "504"
                            ],
                            "Id": "StatusCode",
                            "Type": "CHOICE"
                        },
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "RedirectUrl",
                        "Type": "CUSTOM_STRING"
                    }
                ]
            },
            {
                "Action": "Cache",
                "Properties": [
                    {
                        "ChoiceProperties": [
                            {
                                "ChoicesValue": [
                                    "on",
                                    "off"
                                ],
                                "ExtraParameter": null,
                                "IsAllowEmpty": false,
                                "IsMultiple": false,
                                "Max": 0,
                                "Min": 0,
                                "Name": "Switch",
                                "Type": "TOGGLE"
                            }
                        ],
                        "ChoicesValue": [],
                        "ExtraParameter": null,
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "FollowOrigin",
                        "Type": "OBJECT"
                    },
                    {
                        "ChoiceProperties": [
                            {
                                "ChoicesValue": [
                                    "on",
                                    "off"
                                ],
                                "ExtraParameter": null,
                                "IsAllowEmpty": false,
                                "IsMultiple": false,
                                "Max": 0,
                                "Min": 0,
                                "Name": "Switch",
                                "Type": "TOGGLE"
                            },
                            {
                                "ChoicesValue": [],
                                "ExtraParameter": null,
                                "IsAllowEmpty": false,
                                "IsMultiple": false,
                                "Max": 0,
                                "Min": 0,
                                "Name": "CacheTime",
                                "Type": "CUSTOM_NUM"
                            }
                        ],
                        "ChoicesValue": [],
                        "ExtraParameter": null,
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "Cache",
                        "Type": "OBJECT"
                    },
                    {
                        "ChoiceProperties": [
                            {
                                "ChoicesValue": [
                                    "on",
                                    "off"
                                ],
                                "ExtraParameter": null,
                                "IsAllowEmpty": false,
                                "IsMultiple": false,
                                "Max": 0,
                                "Min": 0,
                                "Name": "Switch",
                                "Type": "TOGGLE"
                            }
                        ],
                        "ChoicesValue": [],
                        "ExtraParameter": null,
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "NoCache",
                        "Type": "OBJECT"
                    }
                ]
            },
            {
                "Action": "MaxAge",
                "Properties": [
                    {
                        "ChoiceProperties": [],
                        "ChoicesValue": [],
                        "ExtraParameter": null,
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "MaxAgeTime",
                        "Type": "CUSTOM_NUM"
                    },
                    {
                        "ChoiceProperties": [],
                        "ChoicesValue": [
                            "on",
                            "off"
                        ],
                        "ExtraParameter": null,
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "FollowOrigin",
                        "Type": "TOGGLE"
                    }
                ]
            },
            {
                "Action": "StatusCodeCache",
                "Properties": [
                    {
                        "ChoiceProperties": [],
                        "ChoicesValue": [],
                        "ExtraParameter": {
                            "Choices": [
                                "403",
                                "404",
                                "404",
                                "405",
                                "414",
                                "416",
                                "451",
                                "500",
                                "501",
                                "502",
                                "503",
                                "504"
                            ],
                            "Id": "StatusCode",
                            "Type": "CHOICE"
                        },
                        "IsAllowEmpty": false,
                        "IsMultiple": false,
                        "Max": 0,
                        "Min": 0,
                        "Name": "CacheTime",
                        "Type": "CUSTOM_NUM"
                    }
                ]
            }
        ]
    }
}
```

