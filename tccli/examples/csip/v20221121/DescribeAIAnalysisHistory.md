**Example 1: 1**



Input: 

```
tccli csip DescribeAIAnalysisHistory --cli-unfold-argument  \
    --Filter.Limit 1 \
    --SessionID 81ed4b6f-**************-0bdcb73e392e
```

Output: 
```
{
    "Response": {
        "SessionList": [
            {
                "IsPinned": true,
                "ModifyTime": 1773628114,
                "SessionID": "2e92a6a4-953b-4565-b8eb-59f69b5beda3",
                "Title": "生成安全周报（存在问题）"
            }
        ],
        "Total": 97,
        "RequestId": "7d2d9c37-2216-4999-a501-813bdbcd1da5"
    }
}
```

