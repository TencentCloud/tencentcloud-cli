**Example 1: success**



Input: 

```
tccli tcbr DescribeCloudRunProcessLog --cli-unfold-argument  \
    --EnvId 字符串 \
    --RunId 字符串
```

Output: 
```
{
    "Response": {
        "Logs": [
            "1"
        ],
        "RequestId": "c531c155-b4bc-4599-8ec3-ee12c403b34e"
    }
}
```

**Example 2: 查询运行日志**



Input: 

```
tccli tcbr DescribeCloudRunProcessLog --cli-unfold-argument  \
    --EnvId test-1gbtbgkjf8f48e2c \
    --RunId 1nSHRvIblNiK4m
```

Output: 
```
{
    "Response": {
        "Logs": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

