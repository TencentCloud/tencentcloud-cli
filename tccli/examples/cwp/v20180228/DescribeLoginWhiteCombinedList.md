**Example 1: 获取登录审计白名单列表-支持新版本筛选**

获取登录审计白名单列表-支持新版本筛选

Input: 

```
tccli cwp DescribeLoginWhiteCombinedList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c",
        "LoginWhiteCombinedInfos": [
            {
                "Id": 357790160,
                "Places": null,
                "UserName": "root",
                "SrcIp": "1.1.1.1",
                "IsGlobal": 0,
                "CreateTime": "2019-12-25 11:57:15",
                "ModifyTime": "2019-12-25 11:57:15",
                "Locale": "",
                "Locations": "",
                "Remark": "",
                "StartTime": "",
                "EndTime": "",
                "Name": "cwp",
                "Desc": "1.1.1.1",
                "Uuid": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
            }
        ]
    }
}
```

