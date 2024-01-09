**Example 1: 查询订阅实例是否可以退换**

查询订阅实例是否可以退换

Input: 

```
tccli dts DescribeSubscribeReturnable --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw
```

Output: 
```
{
    "Response": {
        "IsReturnable": true,
        "ReturnFailMessage": "",
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

