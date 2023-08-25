**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentLatestRiskDetailInfo --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0 \
    --RiskId 0
```

Output: 
```
{
    "Response": {
        "DataSourceId": "abc",
        "DataSourceName": "abc",
        "AssetName": "abc",
        "AssessmentTemplateId": 0,
        "IdentifyTemplateId": 0,
        "RiskType": "abc",
        "RiskName": "abc",
        "RiskDescription": "abc",
        "RiskLevel": "abc",
        "SuggestAction": "abc",
        "Status": 0,
        "Remark": "abc",
        "SecurityProduct": [
            {
                "ProductName": "abc",
                "ReferUrl": "abc"
            }
        ],
        "RiskDimension": "abc",
        "RelationAsset": [
            "abc"
        ],
        "AccountRiskDetail": [
            {
                "Id": "abc",
                "RiskAccount": "abc"
            }
        ],
        "PrivilegeRiskDetail": [
            {
                "AccountName": [
                    "abc"
                ],
                "TableName": "abc",
                "Description": "abc"
            }
        ],
        "PolicyRiskCosFileList": [
            "abc"
        ],
        "AKSKLeak": [
            {
                "AK": "abc",
                "SK": "abc",
                "URL": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

