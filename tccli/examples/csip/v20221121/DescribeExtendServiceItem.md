**Example 1: 查询用户订单信息**

查询用户订单信息

Input: 

```
tccli csip DescribeExtendServiceItem --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Data": [
            {
                "ResourceID": "abc",
                "InquireKey": "abc",
                "LeftNum": 0,
                "InquireUsed": 0,
                "BeginTime": "abc",
                "OrderStatus": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

