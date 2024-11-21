**Example 1: 查询渠道商下属企业额度使用情况**



Input: 

```
tccli trp DescribeCorpQuotas --cli-unfold-argument  \
    --Keyword 10000
```

Output: 
```
{
    "Response": {
        "CorpQuotas": [
            {
                "CorpId": 10000,
                "UsageQuota": {
                    "SaleCnt": 500,
                    "UpdateTime": "2024-10-30T07:16:21.265Z",
                    "CorpId": 10000,
                    "ChainCnt": 50,
                    "FactoryCnt": 10,
                    "RiskCnt": 30,
                    "TrackCnt": 45,
                    "ItemCnt": 400
                },
                "Quota": {
                    "CorpId": 10000,
                    "TrackQuota": 1500,
                    "FactoryQuota": 200,
                    "QuotaId": 110,
                    "SaleQuota": 2000,
                    "Version": "lite",
                    "ItemQuota": 1800,
                    "StartTime": "2024-10-01T07:16:21.265Z",
                    "Services": [
                        "track"
                    ],
                    "RiskQuota": 1200,
                    "EndTime": "2025-10-01T07:16:21.265Z",
                    "TrackType": 1,
                    "ChainQuota": 1400,
                    "ProductCertify": 0
                },
                "CorpName": "企业名称"
            }
        ],
        "Total": 1,
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

