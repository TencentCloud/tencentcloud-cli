**Example 1: 设置记录备注**

 

Input: 

```
tccli dnspod DescribeRecordLineList --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --DomainGrade DP_ULTRA
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "LineGroupList": [
            {
                "LineId": "998=3",
                "Name": "分组2",
                "LineList": [
                    "境外",
                    "第3个_line",
                    "第2个_line"
                ],
                "Type": "user"
            },
            {
                "Name": "东北",
                "LineId": "15=1",
                "LineList": [
                    "黑龙江移动",
                    "黑龙江电信",
                    "黑龙江联通",
                    "吉林移动",
                    "吉林电信",
                    "吉林联通",
                    "辽宁移动",
                    "辽宁电信",
                    "辽宁联通"
                ],
                "Type": "system"
            },
            {
                "Name": "港澳台地区",
                "LineId": "15=7",
                "LineList": [
                    "中国香港",
                    "中国澳门",
                    "中国台湾"
                ],
                "Type": "system"
            }
        ],
        "LineList": [
            {
                "Name": "默认",
                "LineId": "0"
            },
            {
                "Name": "境外",
                "LineId": "3=0"
            },
            {
                "Name": "境内",
                "LineId": "7=0"
            },
            {
                "Name": "电信",
                "LineId": "10=0"
            },
            {
                "Name": "联通",
                "LineId": "10=1"
            }
        ]
    }
}
```

