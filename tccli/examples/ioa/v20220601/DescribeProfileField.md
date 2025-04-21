**Example 1: 查询信息登记数据**



Input: 

```
tccli ioa DescribeProfileField --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "da50c49f-9458-4ae0-9ac9-1bc9a0fa6a4e",
        "Data": {
            "Editable": 0,
            "Enable": 0,
            "Way": "startup",
            "ProfileField": [
                {
                    "IsCustom": 0,
                    "Title": "姓名",
                    "Id": 57
                },
                {
                    "IsCustom": 0,
                    "Title": "部门",
                    "Id": 58
                },
                {
                    "IsCustom": 0,
                    "Title": "电话",
                    "Id": 59
                },
                {
                    "IsCustom": 0,
                    "Title": "邮箱",
                    "Id": 60
                }
            ]
        }
    }
}
```

