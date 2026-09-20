**Example 1: 直播审核图库添加图片**



Input: 

```
tccli live DescribeAuditGroupTag --cli-unfold-argument  \
    --TagType Other
```

Output: 
```
{
    "Response": {
        "GroupTypeList": [
            {
                "GroupClassList": [
                    {
                        "GroupClassEname": "Polity",
                        "GroupClassName": "政治",
                        "LabelGroupList": [
                            {
                                "GroupEname": "PositiveContent",
                                "GroupMsg": "示例：厉害了，我的国！这是祖国崛起的见证",
                                "GroupName": "正面内容"
                            }
                        ]
                    }
                ],
                "TagType": "TagText"
            }
        ],
        "RequestId": "76984f4f-b2a3-4131-9785-6e62bb2907a2"
    }
}
```

