**Example 1: 查询过滤器列表**

查询apitest下所有的过滤器列表

Input: 

```
tccli capioss DescribeFreqLimiterList --cli-unfold-argument  \
    --Data.Module apitest
```

Output: 
```
{
    "Response": {
        "Filters": [
            {
                "Module": "apitest",
                "Name": "$module.$version.$action.$uin",
                "Spec": {
                    "KeyPattern": "$module/$version/$action/$uin",
                    "Matchers": [
                        {
                            "FrequencyLimit": 2,
                            "Matcher": "apitest/2021-10-30/AddHan2/123"
                        },
                        {
                            "FrequencyLimit": 1,
                            "Matcher": "apitest/2021-10-30/AddHan2/*"
                        },
                        {
                            "FrequencyLimit": -1,
                            "Matcher": "*/*/*/*"
                        },
                        {
                            "FrequencyLimit": 1,
                            "Matcher": "apitest/2017-03-12/InstanceTest/*"
                        }
                    ]
                }
            },
            {
                "Module": "apitest",
                "Name": "$module.$version.$action.$uin_group",
                "Spec": {
                    "KeyPattern": "$module/$version/$action/$uin_group",
                    "Matchers": [
                        {
                            "FrequencyLimit": -1,
                            "Matcher": "*/*/*/*"
                        },
                        {
                            "FrequencyLimit": 100,
                            "Matcher": "apitest/2017-03-12/InstanceTest/cloudapi"
                        },
                        {
                            "FrequencyLimit": 50,
                            "Matcher": "apitest/2017-03-12/InstanceTest/yunapi"
                        },
                        {
                            "FrequencyLimit": -1,
                            "Matcher": "apitest/2017-03-12/InstanceTest/*"
                        }
                    ],
                    "UinGroups": [
                        {
                            "GroupName": "cloudapi",
                            "UinList": [
                                "11111",
                                "22222",
                                "33333"
                            ]
                        },
                        {
                            "GroupName": "yunapi",
                            "UinList": [
                                "123",
                                "3333",
                                "89721"
                            ]
                        }
                    ]
                }
            }
        ],
        "RequestId": "c1bae0be-6675-4408-a7ff-0804fcb0b4bb"
    }
}
```

