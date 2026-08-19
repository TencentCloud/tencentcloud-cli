**Example 1: 云资源配置检测标准章节条款树**



Input: 

```
tccli csip DescribeComplianceStandardTermTree --cli-unfold-argument  \
    --StandardID 3 \
    --MemberId mem-00addss \
    --ContentFilter all
```

Output: 
```
{
    "Response": {
        "Chapters": [
            {
                "MenuID": "1",
                "Name": "安全通用要求",
                "Terms": [
                    {
                        "Description": "应采用校验技术保证通信过程中数据的完整性。",
                        "Name": "1.2.2 通信传输",
                        "Rationale": "",
                        "RuleCount": 9,
                        "TermID": 482
                    }
                ]
            }
        ],
        "Name": "网络安全等级保护基本要求（二级）",
        "StandardID": 3,
        "RequestId": "a7bbb82f-1a6c-4589-99c4-749c97e52fde"
    }
}
```

