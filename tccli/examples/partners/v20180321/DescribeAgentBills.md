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
                "OrderId": "xx",
                "ClientUin": "xx",
                "ProjectType": "xx",
                "ClientType": "xx",
                "PayerMode": "xx",
                "ActivityId": "xx",
                "Uin": "xx",
                "PayMode": "xx",
                "ClientRemark": "xx",
                "SettleMonth": "xx",
                "PayTime": "2020-09-22 00:00:00",
                "Amt": 0,
                "GoodsType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

