**Example 1: 示例1**



Input: 

```
tccli ioa DescribeRootGroupId --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9174ff99-833a-4c07-8f44-ae8b6d454428",
        "Data": {
            "RootGroupId": 42631
        }
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeRootGroupId --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "RootGroupId": 92
        },
        "RequestId": "77dea8e5-969c-486e-ae61-23b464cdbb67"
    }
}
```

