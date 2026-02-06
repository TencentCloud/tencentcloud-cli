**Example 1: DescribeLibraDBVersion**

查询只读分析引擎的内核版本

Input: 

```
tccli cynosdb DescribeLibraDBVersion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6cde9959-cf79-4e50-ac59-bb45ebe1634a",
        "VersionList": [
            {
                "HasPermission": true,
                "Tag": "stable",
                "Version": "1.2404.21.0"
            },
            {
                "HasPermission": true,
                "Tag": "beta",
                "Version": "test.119382630"
            },
            {
                "HasPermission": true,
                "Tag": "beta",
                "Version": "1.2404.11.0"
            }
        ]
    }
}
```

