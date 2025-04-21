**Example 1: DescribeAuthPolicy**



Input: 

```
tccli ioa DescribeAuthPolicy --cli-unfold-argument  \
    --GroupId 113 \
    --Condition.PageNum 1 \
    --Condition.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "PolicyType": 2,
                    "PolicyPriority": 1,
                    "Description": "\"认证策略描述\"",
                    "Utime": "",
                    "ScopeItems": [
                        {
                            "ScopeType": 1,
                            "List": []
                        },
                        {
                            "ScopeType": 2,
                            "List": [
                                {
                                    "Id": 113,
                                    "Name": "本地自建-认证联调"
                                }
                            ]
                        },
                        {
                            "ScopeType": 3,
                            "List": []
                        }
                    ],
                    "PcAuthConfig": [
                        {
                            "AuthState": 1,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        }
                    ],
                    "Itime": "2022-07-01 19:39:24",
                    "MobileAuthConfig": [
                        {
                            "AuthState": 1,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        }
                    ],
                    "GroupId": 113,
                    "PolicyId": 14,
                    "PolicyName": "\"认证策略\""
                },
                {
                    "PolicyType": 1,
                    "PolicyPriority": 0,
                    "Description": "",
                    "Utime": "",
                    "ScopeItems": [
                        {
                            "ScopeType": 1,
                            "List": []
                        },
                        {
                            "ScopeType": 2,
                            "List": [
                                {
                                    "Id": 113,
                                    "Name": "本地自建-认证联调"
                                }
                            ]
                        },
                        {
                            "ScopeType": 3,
                            "List": []
                        }
                    ],
                    "PcAuthConfig": [
                        {
                            "AuthState": 1,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        },
                        {
                            "AuthState": 2,
                            "AuthSwitch": 1,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        },
                        {
                            "AuthState": 3,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        }
                    ],
                    "Itime": "2022-07-01 12:42:47",
                    "MobileAuthConfig": [
                        {
                            "AuthState": 1,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        },
                        {
                            "AuthState": 2,
                            "AuthSwitch": 1,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        },
                        {
                            "AuthState": 3,
                            "AuthSwitch": 2,
                            "AdAutoLoginSwitch": 1,
                            "AuthSourceArray": [
                                {
                                    "AuthSourceGuid": "iOA",
                                    "AuthSourceId": 5,
                                    "AuthSourceName": "iOA本地账密"
                                }
                            ],
                            "ExtraConfig": {
                                "AvoidAuthSource": [],
                                "AvoidSecondAuthSwitch": 1
                            }
                        }
                    ],
                    "GroupId": 113,
                    "PolicyId": 13,
                    "PolicyName": "基础策略"
                }
            ],
            "Page": {
                "PageNum": 1,
                "PageSize": 10,
                "Total": 2,
                "PageCount": 1
            }
        },
        "RequestId": "b00dbeb5-7b02-476d-b603-2eaf7bdee42a"
    }
}
```

