**Example 1: 展示合规选项卡**



Input: 

```
tccli sag DescribeComplianceOptionList --cli-unfold-argument  \
    --Os Windows
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "ioa",
                "CheckEnable": 1,
                "RiskLevel": 1,
                "CheckCount": 2
            }
        ],
        "RequestId": "xxx"
    }
}
```

