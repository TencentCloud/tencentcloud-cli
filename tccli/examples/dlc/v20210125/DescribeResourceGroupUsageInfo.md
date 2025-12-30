**Example 1: 查询标准引擎资源组CU使用情况**

查询标准引擎资源CU使用情况

Input: 

```
tccli dlc DescribeResourceGroupUsageInfo --cli-unfold-argument  \
    --SessionId rg-5ga6u6gzxx
```

Output: 
```
{
    "Response": {
        "Available": 40,
        "RequestId": "6068a77d-5538-4e1d-a93f-cf5800c98e1b",
        "Total": 64,
        "Used": 24
    }
}
```

