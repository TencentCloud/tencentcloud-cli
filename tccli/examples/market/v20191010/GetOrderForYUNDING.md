**Example 1: 云鼎-订单查询接口**

提供云鼎-订单查询接口

Input: 

```
tccli market GetOrderForYUNDING --cli-unfold-argument  \
    --EndTime 1 \
    --OwnerUin xx \
    --StartTime 1
```

Output: 
```
{
    "Response": {
        "DataList": [
            {
                "OrderName": "xx",
                "OwnerUin": "xx",
                "OrderCreateTime": "xx",
                "OrderEndTime": "xx",
                "ProductID": 0,
                "ProductName": "xx",
                "RealTotalCost": 0,
                "CycleNum": 0,
                "OrderState": "xx",
                "ProviderUin": "xx",
                "Number": "xx"
            }
        ],
        "Total": 0,
        "RequestId": "xx"
    }
}
```

