**Example 1: 查询命名空间列表**

查询命名空间列表

Input: 

```
tccli tdmq DescribeInternalRocketMQNamespaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Namespaces": [
            {
                "NamespaceId": "xx",
                "RetentionTime": 1,
                "Remark": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

