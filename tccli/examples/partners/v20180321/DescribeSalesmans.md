**Example 1: 成功示例**



Input: 

```
tccli partners DescribeSalesmans --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "92e62a5d-e447-431c-b366-bd84905253f3",
        "AgentSalesmanSet": [
            {
                "Uin": "3286669433",
                "SalesUin": "100009339379",
                "SalesName": "GR",
                "CreateTime": "2019-02-27 16:56:59"
            }
        ],
        "TotalCount": 11
    }
}
```

