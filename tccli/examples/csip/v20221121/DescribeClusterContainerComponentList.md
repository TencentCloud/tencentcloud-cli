**Example 1: 查询容器关联组件列表示例**



Input: 

```
tccli csip DescribeClusterContainerComponentList --cli-unfold-argument  \
    --ContainerId abc123def456
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "List": [
            {
                "Name": "openssl",
                "Version": "1.1.1q"
            }
        ],
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

