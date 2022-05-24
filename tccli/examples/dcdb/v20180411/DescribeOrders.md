**Example 1: 查询订单信息**



Input: 

```
tccli dcdb DescribeOrders --cli-unfold-argument  \
    --DealNames 20181103110163
```

Output: 
```
{
    "Response": {
        "RequestId": "9b59ee51-0e13-1c2f-dedb-59fabe9d7f4a",
        "TotalCount": 1,
        "Deals": [
            {
                "DealName": "20181103110163",
                "OwnerUin": "1235674890",
                "Count": 1,
                "PayMode": 1,
                "FlowId": 1234,
                "InstanceIds": [
                    "dcdbt-avw0207d"
                ]
            }
        ]
    }
}
```

