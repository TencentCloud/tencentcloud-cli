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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "AgentBillSet": [
            {
                "Uin": "11111",
                "OrderId": "20180201112843",
                "ClientUin": "33333",
                "ClientRemark": "",
                "PayTime": "2018-02-01 02:51:02",
                "GoodsType": "云服务器",
                "PayMode": "prepay",
                "SettleMonth": "2018-02",
                "Amt": "19200",
                "PayerMode": "selfpay",
                "ClientType": "assign",
                "ProjectType": ""
            }
        ],
        "TotalCount": 2
    }
}
```

