**Example 1: API资产列表**



Input: 

```
tccli waf DescribeApiListVersionTwo --cli-unfold-argument  \
    --Domain qcloudwaf.com \
    --Filters.0.Entity key \
    --Filters.0.Operator = \
    --Filters.0.Value waf \
    --PageIndex 0 \
    --PageSize 0 \
    --Sort timestamp \
    --NeedTotalCount True \
    --StartTs 0 \
    --EndTs 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Domain": "qcloudwaf.com",
                "Method": "GET",
                "ApiName": "/test/aa",
                "Scene": "login",
                "Label": [
                    "login"
                ],
                "Active": true,
                "Timestamp": 123131231123,
                "InsertTime": 123131312321,
                "Mode": "1",
                "Level": "300",
                "Count": 1,
                "Remark": "adasd",
                "IsAuth": 0,
                "ApiRequestRuleId": 0,
                "ApiLimitRuleId": 0
            }
        ],
        "Total": 0,
        "RequestId": "asdq2we41234123cszd"
    }
}
```

