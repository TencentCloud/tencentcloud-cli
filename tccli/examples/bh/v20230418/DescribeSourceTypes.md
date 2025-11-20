**Example 1: 获取认证源信息**



Input: 

```
tccli bh DescribeSourceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SourceTypeSet": [
            {
                "Type": "test",
                "Name": "钉钉",
                "Source": 1001,
                "Target": "mini_iam"
            }
        ],
        "RequestId": "cf85w9eee-b651-4ff3q-9b49-173f9f55733f"
    }
}
```

