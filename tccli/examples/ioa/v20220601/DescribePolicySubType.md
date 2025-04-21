**Example 1: 查询策略子类型**



Input: 

```
tccli ioa DescribePolicySubType --cli-unfold-argument  \
    --OsType 0 \
    --PolicyType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "45862402-3d29-49db-80ec-4bd38a7864e2",
        "Data": [
            {
                "Description": "",
                "PolicySubType": 0,
                "PolicyTotal": 6,
                "Os": [
                    0
                ],
                "PolicySubName": "全部策略"
            },
            {
                "Description": "",
                "PolicySubType": 1,
                "PolicyTotal": 1,
                "Os": [
                    0,
                    1,
                    2
                ],
                "PolicySubName": "病毒查杀"
            },
            {
                "Description": "",
                "PolicySubType": 2,
                "PolicyTotal": 1,
                "Os": [
                    0,
                    1
                ],
                "PolicySubName": "实时防护"
            },
            {
                "Description": "",
                "PolicySubType": 4,
                "PolicyTotal": 1,
                "Os": [
                    0
                ],
                "PolicySubName": "漏洞修复"
            },
            {
                "Description": "",
                "PolicySubType": 5,
                "PolicyTotal": 1,
                "Os": [
                    0,
                    2
                ],
                "PolicySubName": "信息采集"
            },
            {
                "Description": "",
                "PolicySubType": 6,
                "PolicyTotal": 1,
                "Os": [
                    0
                ],
                "PolicySubName": "文档保护"
            },
            {
                "Description": "",
                "PolicySubType": 29,
                "PolicyTotal": 1,
                "Os": [
                    0
                ],
                "PolicySubName": "横向渗透防护"
            }
        ]
    }
}
```

