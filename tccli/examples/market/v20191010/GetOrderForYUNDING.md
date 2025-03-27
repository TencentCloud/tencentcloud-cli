**Example 1: 云鼎-订单查询接口**

提供云鼎-订单查询接口

Input: 

```
tccli market GetOrderForYUNDING --cli-unfold-argument  \
    --EndTime 1 \
    --OwnerUin xdx \
    --StartTime 1
```

Output: 
```
{
    "Response": {
        "DataList": [
            {
                "OrderName": "name",
                "OwnerUin": "name",
                "OrderCreateTime": "name",
                "OrderEndTime": "name",
                "ProductID": 0,
                "ProductName": "name",
                "RealTotalCost": 0,
                "CycleNum": 0,
                "OrderState": "name",
                "ProviderUin": "name",
                "Number": "name"
            }
        ],
        "Total": 0,
        "RequestId": "name"
    }
}
```

