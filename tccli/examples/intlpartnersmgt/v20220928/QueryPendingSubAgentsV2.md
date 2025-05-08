**Example 1: 查询申请中二级经销商信息**



Input: 

```
tccli intlpartnersmgt QueryPendingSubAgentsV2 --cli-unfold-argument  \
    --Page 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "Status": "Reviewing",
                "SubAgentUin": 2000000000,
                "Name": "张三",
                "Mobile": "188****8888",
                "ApplyTime": "2023-01-03 12:11:32",
                "MaterialUrl": "xx.abc.cos.com",
                "Email": "abc@gmail.com"
            }
        ],
        "RequestId": "abc45-****-sjncek2-kdng****"
    }
}
```

