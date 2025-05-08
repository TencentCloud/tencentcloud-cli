**Example 1: 查询一级经销商间接子客**



Input: 

```
tccli intlpartnersmgt QueryT1IndirectCustomersDetail --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --SubAgentUin 200000000000
```

Output: 
```
{
    "Response": {
        "RequestId": "********",
        "Total": 1,
        "SubAgentUin": 200000000000,
        "SubAgentName": "张三",
        "Data": [
            {
                "ClientUin": 200000000001,
                "ClientName": "李四",
                "ClientBindTime": "2024-02-02 09:25:38"
            }
        ]
    }
}
```

