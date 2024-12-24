**Example 1: 示例**

查询最新风险项详情数据

Input: 

```
tccli dsgc DescribeDSPAAssessmentLatestRiskDetailInfo --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --TemplateId 1 \
    --RiskId 1
```

Output: 
```
{
    "Response": {
        "DataSourceId": "mariadb-a1b2c3d4",
        "DataSourceName": "订单数据库",
        "AssetName": "casb001",
        "AssessmentTemplateId": 12,
        "IdentifyTemplateId": 3,
        "RiskType": "account_risk",
        "RiskName": "数据库高危账户权限",
        "RiskDescription": "云数据库应用账号（非root账户）拥有高危权限，误操作或被利用导致业务发生严重故障，例如DROP权限，删表删库",
        "RiskLevel": "high",
        "SuggestAction": "1. 访问腾讯云数据库。2. >若应用账号（非root账户）下的高危权限（DROP）不再使用",
        "Status": 0,
        "Remark": "风险备注",
        "SecurityProduct": [
            {
                "ProductName": "数据安全审计",
                "ReferUrl": "https://console.cloud.tencent.com/cds/overview"
            }
        ],
        "RiskDimension": "install",
        "RelationAsset": [
            "cdb-a1b2c3d4"
        ],
        "AccountRiskDetail": [
            {
                "Id": "1",
                "RiskAccount": "cdb-a3b7c81"
            }
        ],
        "PrivilegeRiskDetail": [
            {
                "AccountName": [
                    "root"
                ],
                "TableName": "test_tb",
                "Description": "账号风险详情"
            }
        ],
        "PolicyRiskCosFileList": [
            "cos-129as90ajcwer29hca241naqx546"
        ],
        "AKSKLeak": [
            {
                "AK": "a1b2c3d45f6e32ac3ed",
                "SK": "a1b2c3d45f6e32ac3ed",
                "URL": "http://console.tencent.com.cn"
            }
        ],
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

