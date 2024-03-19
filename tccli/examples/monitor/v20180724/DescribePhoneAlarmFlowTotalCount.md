**Example 1: 查询周期内电话流水总数**



Input: 

```
tccli monitor DescribePhoneAlarmFlowTotalCount --cli-unfold-argument  \
    --Module monitor \
    --QueryTime 1659893700
```

Output: 
```
{
    "Response": {
        "Count": 10,
        "RequestId": "59464af9-4da8-49de-a692-49d2371f0b38"
    }
}
```

