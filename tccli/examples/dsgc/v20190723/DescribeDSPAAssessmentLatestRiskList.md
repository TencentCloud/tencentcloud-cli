**Example 1: 示例**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentLatestRiskList --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 2 \
    --Limit 0 \
    --Offset abc \
    --DataSourceId abc \
    --RiskType abc \
    --ControlItemId abc \
    --Status 0 \
    --BeginTime abc \
    --EndTime abc \
    --RiskLevel abc
```

Output: 
```
{
    "Response": {
        "LatestRiskList": [
            {
                "Id": 0,
                "DataSourceId": "abc",
                "DataSourceName": "abc",
                "DataSourceType": "abc",
                "AssetName": "abc",
                "RiskType": "abc",
                "RiskName": "abc",
                "RiskLevel": "abc",
                "RiskDescription": "abc",
                "SuggestAction": "abc",
                "SecurityProduct": [
                    {
                        "ProductName": "abc",
                        "ReferUrl": "abc"
                    }
                ],
                "Status": 0,
                "ScanTime": "abc",
                "LastProcessTime": "abc",
                "IdentifyComplianceId": 0,
                "ItemSubType": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

