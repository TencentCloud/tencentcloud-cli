**Example 1: 获取本地提权规则列表**

获取本地提权规则列表

Input: 

```
tccli yunjing DescribePrivilegeRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "List": [
            {
                "Id": 2,
                "Uuid": "6b13beb4-be6e-11e9-a040-40f2e9f5c7d2",
                "ProcessName": "first2",
                "SMode": 1,
                "Operator": "console",
                "IsGlobal": 0,
                "Status": 0,
                "CreateTime": "2019-08-23 15:26:05",
                "ModifyTime": "2019-08-23 15:26:05"
            }
        ],
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

