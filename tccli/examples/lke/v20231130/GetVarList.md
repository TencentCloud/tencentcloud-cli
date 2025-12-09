**Example 1: 获取应用下的变量列表**

获取应用下的变量列表

Input: 

```
tccli lke GetVarList --cli-unfold-argument  \
    --AppBizId 1793260396881641472
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VarId": "55127e9e-6e9e-4c11-bcf8-b524959cd841",
                "VarName": "TimeIDUpdate",
                "VarDesc": "时间ID描述",
                "VarType": "STRING",
                "VarDefaultValue": "2025-05-14",
                "VarDefaultFileName": ""
            },
            {
                "VarId": "d125c28b-55db-4478-9066-6115ab97ee17",
                "VarName": "UserID",
                "VarDesc": "用户ID描述",
                "VarType": "STRING",
                "VarDefaultValue": "6213673423",
                "VarDefaultFileName": ""
            }
        ],
        "RequestId": "925208e7-46fa-43b3-a429-ddcbccad24f6",
        "Total": 2
    }
}
```

