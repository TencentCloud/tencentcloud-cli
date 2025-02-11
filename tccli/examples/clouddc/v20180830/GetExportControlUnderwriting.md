**Example 1: 通过测算单获取出口管制、专利风险管制**



Input: 

```
tccli clouddc GetExportControlUnderwriting --cli-unfold-argument  \
    --EstimateCodeList abc
```

Output: 
```
{
    "Response": {
        "EstimateList": [
            {
                "EstimateCode": "Q2024042214686",
                "IsExportControl": 0,
                "IsPatentRiskControl": 1
            },
            {
                "EstimateCode": "Q20240428147L4-01-01",
                "IsExportControl": 0,
                "IsPatentRiskControl": 1
            },
            {
                "EstimateCode": "Q2023021012HHQ",
                "IsExportControl": 0,
                "IsPatentRiskControl": 1
            },
            {
                "EstimateCode": "Q20230724133AQ",
                "IsExportControl": 0,
                "IsPatentRiskControl": 1
            },
            {
                "EstimateCode": "Q20230706130YU",
                "IsExportControl": 0,
                "IsPatentRiskControl": 1
            }
        ],
        "RequestId": "1f9dde13-0059-4d6b-9c18-f3a4a6eefa49"
    }
}
```

