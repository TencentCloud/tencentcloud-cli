**Example 1: 查询云数据库实例的当前操作**



Input: 

```
tccli mongodb DescribeCurrentOp --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5
```

Output: 
```
{
    "Response": {
        "RequestId": "302530d2-ee57-495e-89d0-51e03b11815e",
        "TotalCount": 19
    }
}
```

