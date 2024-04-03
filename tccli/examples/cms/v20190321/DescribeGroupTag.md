**Example 1: 正常调用**



Input: 

```
tccli cms DescribeGroupTag --cli-unfold-argument  \
    --HideStatus true \
    --TagType TagAudio
```

Output: 
```
{
    "Response": {
        "GroupTypeList": [
            {
                "TagType": "TagAudio",
                "GroupClassList": [
                    {
                        "GroupClassEname": "Polity",
                        "GroupClassName": "政治",
                        "LabelGroupList": []
                    },
                    {
                        "GroupClassEname": "Porn",
                        "GroupClassName": "色情",
                        "LabelGroupList": []
                    },
                    {
                        "GroupClassEname": "Moan",
                        "GroupClassName": "娇喘",
                        "LabelGroupList": [
                            {
                                "GroupEname": "OVR",
                                "GroupName": "低俗语音识别",
                                "GroupMsg": "示例：呻吟、娇喘、娇喘等性暗示相关的语音"
                            }
                        ]
                    },
                    {
                        "GroupClassEname": "Terror",
                        "GroupClassName": "暴恐",
                        "LabelGroupList": []
                    },
                    {
                        "GroupClassEname": "Illegal",
                        "GroupClassName": "违法",
                        "LabelGroupList": [
                            {
                                "GroupEname": "Illegal",
                                "GroupName": "违法违规内容",
                                "GroupMsg": ""
                            }
                        ]
                    },
                    {
                        "GroupClassEname": "Abuse",
                        "GroupClassName": "谩骂",
                        "LabelGroupList": []
                    },
                    {
                        "GroupClassEname": "Ad",
                        "GroupClassName": "广告",
                        "LabelGroupList": []
                    }
                ]
            }
        ],
        "RequestId": "0411564c-0101-4bd0-8db8-6c4e4bd59b78"
    }
}
```

**Example 2: 标签组数据返回试例**

用于策略维护里面的标签组的选择界面显示分类的数据

Input: 

```
tccli cms DescribeGroupTag --cli-unfold-argument  \
    --HideStatus True \
    --TagType xx
```

Output: 
```
{
    "Response": {
        "GroupTypeList": [
            {
                "GroupClassList": [
                    {
                        "LabelGroupList": [
                            {
                                "GroupEname": "xx",
                                "GroupMsg": "xx",
                                "GroupName": "xx"
                            }
                        ],
                        "GroupClassName": "xx",
                        "GroupClassEname": "xx"
                    }
                ],
                "TagType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

