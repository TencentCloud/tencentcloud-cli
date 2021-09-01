**Example 1: 查询客户余额**



Input: 

```
tccli partners DescribeClientBalanceNew --cli-unfold-argument  \
    --ClientUin 125****938
```

Output: 
```
{
    "Response": {
        "RequestId": "eeedc7d9-2310-4b77-bd3e-23f077e44b7d",
        "Balance": 40,
        "Cash": 40
    }
}
```

