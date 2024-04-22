**Example 1: DescribeBillSummary**

子客计费中心L1账单的api

POST / HTTP/1.1
Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBillSummary
<公共请求参数>

Input: 

```
tccli intlpartnersmgt DescribeBillSummary --cli-unfold-argument  \
    --Month 2023-10 \
    --GroupType tag \
    --TagKey abc
```

Output: 
```
{
    "Response": {
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCodeName": "CVM Dedicated Host",
                        "BusinessCode": "p_cdh",
                        "OriginalCost": "abc",
                        "VoucherPayAmount": "1.1",
                        "RICost": "0.1",
                        "TotalCost": "12.1"
                    }
                ],
                "OriginalCost": "12.1",
                "VoucherPayAmount": "1.1",
                "RICost": "1.1",
                "TotalCost": "2.2",
                "GroupKey": "0",
                "GroupValue": "default"
            }
        ],
        "RequestId": "abc"
    }
}
```

