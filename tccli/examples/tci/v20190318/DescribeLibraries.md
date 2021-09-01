**Example 1: 拉取人员库列表**

拉取人员库列表

Input: 

```
tccli tci DescribeLibraries --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "23dc79d5-c90a-4455-9eee-203cdb6810ed",
        "TotalCount": 4,
        "LibrarySet": [
            {
                "LibraryId": "library_1552907886376820469",
                "LibraryName": "xxx",
                "CreateTime": "0001-01-01T00:00:00+08:00",
                "UpdateTime": "0001-01-01T00:00:00+08:00"
            },
            {
                "LibraryId": "library_155297948085170220399",
                "LibraryName": "xxx",
                "CreateTime": "2019-03-19T15:11:21+08:00",
                "UpdateTime": "2019-03-19T15:11:21+08:00"
            },
            {
                "LibraryId": "library_155297959592861320399",
                "LibraryName": "xxx",
                "CreateTime": "2019-03-19T15:13:16+08:00",
                "UpdateTime": "2019-03-19T15:13:16+08:00"
            },
            {
                "LibraryId": "library_155298561479521165545",
                "LibraryName": "xxx",
                "CreateTime": "2019-03-19T16:53:35+08:00",
                "UpdateTime": "2019-03-19T16:53:35+08:00"
            }
        ]
    }
}
```

