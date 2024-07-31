**Example 1: 获取集团服务设置列表**

获取集团服务设置列表

Input: 

```
tccli organization ListOrganizationService --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ServiceId": 1,
                "ProductName": "云审计",
                "IsAssign": 1,
                "CanAssignCount": 5,
                "Description": "test",
                "MemberNum": "0",
                "Document": "HTTP://XXX",
                "ConsoleUrl": "",
                "IsUsageStatus": 2
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1,
        "AssignManageTotal": 2
    }
}
```

