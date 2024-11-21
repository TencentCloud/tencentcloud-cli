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
                "Id": 10001,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "ProcessName": "privilege",
                "SMode": 1,
                "Operator": "zhangsan",
                "Status": 0,
                "IsGlobal": 0,
                "CreateTime": "2024-08-23 17:13:47",
                "ModifyTime": "2024-08-23 17:13:47",
                "Hostip": "1.1.1.1"
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

