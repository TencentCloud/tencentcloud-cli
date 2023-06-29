**Example 1: 查询直接子客信用**



Input: 

```
tccli intlpartnersmgt QueryDirectCustomersCredit --cli-unfold-argument ```

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

