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
            "DimCntList": [
                {
                    "Dim": 1,
                    "Cnt": 1
                }
            ],
            "TotalCnt": 1
        },
        "RequestId": "xx"
    }
}
```

