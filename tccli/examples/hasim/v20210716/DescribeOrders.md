**Example 1: 查询订单列表**

查询订单列表

Input: 

```
tccli hasim DescribeOrders --cli-unfold-argument  \
    --DealName xx \
    --AuditStatus 0 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "List": [
                {
                    "BigDealId": "20220624194001025501251",
                    "DealName": "20220624194001025501261",
                    "CreatedAt": "2022-06-24T17:49:12+08:00",
                    "Uin": "xxx",
                    "IndustryCode": "工业产品-家居",
                    "Address": "**********",
                    "Contact": "*******",
                    "Msisdn": "**********",
                    "Specification": "5*6贴片两网（多芯片版）",
                    "Comment": "物联网中心",
                    "AuditStatus": "待审核",
                    "FlowStatus": "",
                    "Remark": ""
                }
            ]
        },
        "RequestId": "82b1fc3d-9881-423e-bdf8-d6061f36ec42"
    }
}
```

