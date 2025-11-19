**Example 1: 查询是否开启地域粒度防误删开关**



Input: 

```
tccli vpc DescribeNatGatewayDeletionCheckFlag --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Region": "ap-guangzhou",
        "DeletionCheckFlag": true,
        "RequestId": "12345678-1234-1234-1234-123456789012"
    }
}
```

