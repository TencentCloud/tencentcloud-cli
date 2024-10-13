**Example 1: test3**



Input: 

```
tccli waf DescribeApiListVersionTwo --cli-unfold-argument  \
    --PageIndex 0 \
    --Domain hzh.qcloud.com \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "05f0b0dc-cc07-4ed2-b60f-225169a3d76d",
        "Data": [],
        "Total": 0
    }
}
```

**Example 2: API资产列表**



Input: 

```
tccli waf DescribeApiListVersionTwo --cli-unfold-argument  \
    --Domain abc \
    --Filters.0.Entity abc \
    --Filters.0.Operator abc \
    --Filters.0.Value abc \
    --PageIndex 0 \
    --PageSize 0 \
    --Sort abc \
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
                "Domain": "abc",
                "Method": "abc",
                "ApiName": "abc",
                "Scene": "abc",
                "Label": [
                    "abc"
                ],
                "Active": true,
                "Timestamp": 1,
                "InsertTime": 1,
                "Mode": "abc",
                "Level": "abc",
                "Count": 1,
                "Remark": "abc",
                "IsAuth": 0,
                "ApiRequestRuleId": 0,
                "ApiLimitRuleId": 0
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

