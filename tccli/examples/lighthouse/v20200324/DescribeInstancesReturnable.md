**Example 1: 查询可退还实例**



Input: 

```
tccli lighthouse DescribeInstancesReturnable --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw lhins-xusdke45
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceReturnableSet": [
            {
                "InstanceId": "lhins-ruy9d2tw",
                "IsReturnable": true,
                "ReturnFailCode": 0,
                "ReturnFailMessage": "可以退还"
            },
            {
                "InstanceId": "lhins-xusdke45",
                "IsReturnable": false,
                "ReturnFailCode": 2,
                "ReturnFailMessage": "资源已过期"
            }
        ],
        "RequestId": "3ea94867-0d80-4d22-8ba5-a8d9355efca8"
    }
}
```

