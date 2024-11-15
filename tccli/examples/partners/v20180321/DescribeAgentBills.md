**Example 1: 查询代理商指定月份业务明细**

查询某代理商2018年2月份业务明细

Input: 

```
tccli partners DescribeAgentBills --cli-unfold-argument  \
    --SettleMonth 2018-02
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AgentBillSet": [
            {
                "ActivityId": "0",
                "Amt": 125,
                "ClientRemark": "有特批",
                "ClientType": "old",
                "ClientUin": "2000002",
                "GoodsType": "购买云服务",
                "OrderId": "202401311730494235252",
                "PayMode": "prepay",
                "PayTime": "2024-01-31 06:06:46",
                "PayerMode": "selfpay",
                "ProjectType": "platform",
                "SettleMonth": "2024-01",
                "Uin": "1000001"
            }
        ],
        "RequestId": "84a1e38a-95a1-4cc4-ac7d-232a2d872d45"
    }
}
```

