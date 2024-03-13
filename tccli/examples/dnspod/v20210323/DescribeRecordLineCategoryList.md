**Example 1: 按分类返回线路列表参数示例**

按分类返回线路列表

Input: 

```
tccli dnspod DescribeRecordLineCategoryList --cli-unfold-argument  \
    --Domain dnspod.cn \
    --DomainId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "LineList": [
            {
                "Grade": "DP_FREE",
                "LineId": "0",
                "LineName": "默认",
                "Lines": null,
                "SubGroup": null,
                "Useful": true
            },
            {
                "Grade": "DP_FREE",
                "LineId": "10=0",
                "LineName": "电信",
                "Lines": null,
                "SubGroup": [
                    {
                        "Grade": "DP_FREE",
                        "LineId": "10=0",
                        "LineName": "电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": true
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=0",
                        "LineName": "安徽电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=2",
                        "LineName": "北京电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=4",
                        "LineName": "重庆电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=6",
                        "LineName": "福建电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=8",
                        "LineName": "甘肃电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=10",
                        "LineName": "广东电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=12",
                        "LineName": "广西电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=14",
                        "LineName": "贵州电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=16",
                        "LineName": "海南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=18",
                        "LineName": "河北电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=20",
                        "LineName": "河南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=22",
                        "LineName": "黑龙江电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=24",
                        "LineName": "湖北电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=26",
                        "LineName": "湖南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=28",
                        "LineName": "吉林电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=30",
                        "LineName": "江苏电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=32",
                        "LineName": "江西电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=34",
                        "LineName": "辽宁电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=36",
                        "LineName": "内蒙电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=38",
                        "LineName": "宁夏电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=40",
                        "LineName": "青海电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=42",
                        "LineName": "山东电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=44",
                        "LineName": "山西电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=46",
                        "LineName": "陕西电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=48",
                        "LineName": "上海电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=50",
                        "LineName": "四川电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=52",
                        "LineName": "天津电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=54",
                        "LineName": "西藏电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=56",
                        "LineName": "新疆电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=58",
                        "LineName": "云南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "20=60",
                        "LineName": "浙江电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=0",
                        "LineName": "华北电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=4",
                        "LineName": "东北电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=8",
                        "LineName": "华东电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=12",
                        "LineName": "华中电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=16",
                        "LineName": "华南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=20",
                        "LineName": "西南电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    },
                    {
                        "Grade": "DP_EXPERT",
                        "LineId": "16=24",
                        "LineName": "西北电信",
                        "Lines": null,
                        "SubGroup": null,
                        "Useful": false
                    }
                ],
                "Useful": true
            }
        ]
    }
}
```

