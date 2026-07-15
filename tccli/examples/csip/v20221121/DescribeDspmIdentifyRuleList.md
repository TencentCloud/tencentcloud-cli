**Example 1: 查询dspm数据识别数据项列表**



Input: 

```
tccli csip DescribeDspmIdentifyRuleList --cli-unfold-argument  \
    --MemberId mem-829jduqa \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Description": "自定义描述",
                "Id": 5929,
                "Name": "自定义",
                "Status": 1,
                "Type": 1,
                "UpdateTime": "2026-04-27 17:51:34"
            }
        ],
        "TotalCount": 1,
        "RequestId": "a439d1f6-3598-4010-9192-921d2d12a788"
    }
}
```

