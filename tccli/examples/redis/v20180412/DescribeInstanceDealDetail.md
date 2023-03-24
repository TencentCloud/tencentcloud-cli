**Example 1: 请求示例**

查询订单信息

Input: 

```
tccli redis DescribeInstanceDealDetail --cli-unfold-argument  \
    --DealIds 6959052
```

Output: 
```
{
    "Response": {
        "DealDetails": [
            {
                "DealId": "6959052",
                "DealName": "20181101110365",
                "ZoneId": 100002,
                "GoodsNum": 1,
                "Creater": "1817983094",
                "CreatTime": "2018-11-01 21:12:05",
                "OverdueTime": "2018-11-16 21:12:05",
                "EndTime": "2018-11-01 21:13:18",
                "Status": 4,
                "Description": "发货成功",
                "Price": 91949,
                "InstanceIds": [
                    "crs-bz8prb7x"
                ]
            }
        ],
        "RequestId": "5d739ed7-af13-489f-b005-aaa57aeaf022"
    }
}
```

