**Example 1: 查询用户列表信用**



Input: 

```
tccli intlpartnersmgt QueryCreditByUinList --cli-unfold-argument  \
    --UinList 10000 100001
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RemainingCredit": 0.01,
                "TotalCredit": 100.01,
                "Uin": 1
            },
            {
                "RemainingCredit": 0.01,
                "TotalCredit": 100.01,
                "Uin": 1
            }
        ],
        "RequestId": "0abe4d4f7fdb79c9829d945c2161ff9b"
    }
}
```

