**Example 1: 获取已审核客户列表**



Input: 

```
tccli partners DescribeAgentAuditedClients --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c5d1d9fc-0ecb-495d-98bb-f8a1eee37a22",
        "AgentClientSet": [
            {
                "Uin": "3286669433",
                "ClientUin": "2461871653",
                "ClientRemark": "",
                "ClientName": "2461871653",
                "ClientFlag": "a",
                "AuthType": "-1",
                "AgentTime": "1476195568",
                "AppId": "1252765299",
                "LastMonthAmt": 0,
                "ThisMonthAmt": 0,
                "HasOverdueBill": 0,
                "ClientType": "new",
                "ProjectType": "self",
                "SalesUin": "100009484937",
                "SalesName": "sales2",
                "Mail": "100*****@qq.com"
            }
        ],
        "TotalCount": 9
    }
}
```

