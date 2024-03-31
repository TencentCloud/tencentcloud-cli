**Example 1: 规则触发维度情况**



Input: 

```
tccli wedata DescribeRuleDimStat --cli-unfold-argument  \
    --ProjectId 1 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCnt": 1,
            "DimCntList": [
                {
                    "Dim": 1,
                    "Cnt": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

