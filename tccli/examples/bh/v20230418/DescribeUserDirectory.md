**Example 1: 获取用户目录**



Input: 

```
tccli bh DescribeUserDirectory --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserDirSet": [
            {
                "Id": 43,
                "DirId": 35122,
                "DirName": "钉钉",
                "Source": 1001,
                "SourceName": "钉钉",
                "CreateTime": "2025-04-22T00:00:00+00:00",
                "UserTotal": 34
            }
        ],
        "RequestId": "cf85w9eee-b651-4ff3q-9b49-173f9f55733f"
    }
}
```

