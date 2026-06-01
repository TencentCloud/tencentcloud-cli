**Example 1: 测试示例**



Input: 

```
tccli tchousex DescribeNextEventId --cli-unfold-argument  \
    --InstanceId instance-yxin6btv \
    --ExtParameters.0.Name UserName \
    --ExtParameters.0.Value root \
    --ExtParameters.1.Name Password \
    --ExtParameters.1.Value test
```

Output: 
```
{
    "Response": {
        "NextEventId": 4,
        "RequestId": "8bf4534a-db0d-4480-bb89-bfa757b3fa8c"
    }
}
```

