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
                "CorpId": 1,
                "UsageQuota": {
                    "SaleCnt": 0,
                    "UpdateTime": "xx",
                    "CorpId": 1,
                    "ChainCnt": 0,
                    "FactoryCnt": 0,
                    "RiskCnt": 0,
                    "TrackCnt": 0,
                    "ItemCnt": 0
                },
                "Quota": {
                    "CorpId": 1,
                    "TrackQuota": 0,
                    "FactoryQuota": 0,
                    "QuotaId": 1,
                    "SaleQuota": 0,
                    "Version": "xx",
                    "ItemQuota": 0,
                    "StartTime": "xx",
                    "Services": [
                        "xx"
                    ],
                    "RiskQuota": 0,
                    "EndTime": "xx",
                    "TrackType": 0,
                    "ChainQuota": 0
                },
                "CorpName": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

