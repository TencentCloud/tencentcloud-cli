**Example 1: 查询企业严重违法列表**

查询企业严重违法列表

Input: 

```
tccli eportrait DescribeSeriousIllegals --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Eid 00180b23aa1de3b0c1d04a90ea0eec40
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Eid": "00180b23aa1de3b0c1d04a90ea0eec40",
                "Execution": [
                    {
                        "InDate": "2022-07-21",
                        "InReason": "被列入经营异常名录届满3年仍未履行相关义务的"
                    },
                    {
                        "InDate": "2020-07-18",
                        "InReason": "被列入经营异常名录届满3年仍未履行相关义务的"
                    },
                    {
                        "InDate": "2021-07-13",
                        "InReason": "被列入经营异常名录届满3年仍未履行相关义务的"
                    }
                ]
            }
        ],
        "RequestId": "128d95ec-db21-4643-8ffa-4d30cbe4ec56",
        "TotalCount": 1
    }
}
```

