**Example 1: 查询模块定制使用情况**



Input: 

```
tccli ioa DescribeModuleConfigUsage --cli-unfold-argument  \
    --OsType 0 \
    --SubType 17 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c3608b3b-9b62-4ce7-bed7-92aa6d49c687",
        "Data": {
            "Has": true
        }
    }
}
```

