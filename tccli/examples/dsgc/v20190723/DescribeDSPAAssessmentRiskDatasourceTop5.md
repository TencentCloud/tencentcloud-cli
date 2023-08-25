**Example 1: 受影响资产TOP5统计**

受影响资产TOP5统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDatasourceTop5 --cli-unfold-argument  \
    --DspaId dspa-92aabacd
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "RiskNum": 22,
                "ItemName": "ins-xezz0kz5-aae7c346"
            },
            {
                "RiskNum": 20,
                "ItemName": "cynosdbmysql-9lo12zih"
            },
            {
                "RiskNum": 4,
                "ItemName": "ins-xezz0kz5-ae30f65e"
            },
            {
                "RiskNum": 4,
                "ItemName": "lb-05q58vty-b0bcba42"
            },
            {
                "RiskNum": 2,
                "ItemName": "lb-05q58vty-a38da60b"
            }
        ],
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

