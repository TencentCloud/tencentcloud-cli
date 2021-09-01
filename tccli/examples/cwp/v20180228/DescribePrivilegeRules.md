**Example 1: 获取本地提权规则列表**

获取本地提权规则列表

Input: 

```
tccli cwp DescribePrivilegeRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 1,
                "ModifyTime": "xx",
                "Uuid": "xx",
                "SMode": 1,
                "IsGlobal": 1,
                "CreateTime": "xx",
                "ProcessName": "xx",
                "Hostip": "xx",
                "Operator": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

