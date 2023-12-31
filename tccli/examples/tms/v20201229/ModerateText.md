**Example 1: 客制标签文本内容审核**

用于客户自有标签体系的内容审核，审核结果会以客户定义的标签体系输出结果

Input: 

```
tccli tms ModerateText --cli-unfold-argument  \
    --Content 5Yqg5oiR5aW95Y+LIOe7meS9oOS8mOaDoOWIuA== \
    --BizType test
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "DataId": "123",
        "BizType": "test",
        "Label": {
            "Code": "20003001001",
            "Grade1": "广告",
            "Grade2": "电商广告",
            "Grade3": "拍拍网"
        },
        "TcLabelCodes": [
            "20001001001",
            "20001001002",
            "20001001003"
        ],
        "Suggestion": "Block",
        "Keywords": [
            "优惠券"
        ],
        "ModerationDetails": [
            {
                "Label": {
                    "Code": "20003001001",
                    "Grade1": "广告",
                    "Grade2": "电商广告",
                    "Grade3": "拍拍网"
                },
                "TcLabelCodes": [
                    "20001001001",
                    "20001001002",
                    "20001001003"
                ],
                "LibResults": [
                    {
                        "Keyword": "123",
                        "Positions": [
                            {
                                "Start": 1,
                                "End": 3
                            }
                        ],
                        "LibId": "",
                        "LibName": "",
                        "LibType": 0
                    }
                ],
                "ModelResults": [
                    {
                        "Content": "123",
                        "Positions": [
                            {
                                "Start": 1,
                                "End": 3
                            }
                        ]
                    }
                ],
                "Suggestion": "Block",
                "Score": 80
            }
        ]
    }
}
```

