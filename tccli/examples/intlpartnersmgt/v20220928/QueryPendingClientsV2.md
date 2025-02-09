**Example 1: 查询申请中子客信息**



Input: 

```
tccli intlpartnersmgt QueryPendingClientsV2 --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "Data": [
            {
                "ClientUin": "20000000000",
                "Name": "tom",
                "Type": "A",
                "Mobile": "188****1234",
                "Email": "abc@gmail.com",
                "ApplyTime": "2024-01-03 15:11:10",
                "Status": "Reviewing"
            }
        ],
        "RequestId": "0aa8fe2c-****-4d94-b481-3f329******a"
    }
}
```

