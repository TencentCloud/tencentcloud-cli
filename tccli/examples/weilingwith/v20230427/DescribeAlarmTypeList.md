**Example 1: 告警状态列表**

成功响应

Input: 

```
tccli weilingwith DescribeAlarmTypeList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "3840c20f-f364-4569-8120-1c29f072dd24",
        "Result": {
            "AlarmTypeSet": [
                {
                    "EnglishName": "excessive",
                    "Id": 26,
                    "Name": "人流数量异常",
                    "ParentId": 25,
                    "Type": 1
                }
            ]
        }
    }
}
```

