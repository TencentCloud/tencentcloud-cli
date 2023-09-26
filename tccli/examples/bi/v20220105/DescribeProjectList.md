**Example 1: 项目列表数据接口**

项目列表数据接口

Input: 

```
tccli bi DescribeProjectList --cli-unfold-argument  \
    --PageSize 1 \
    --PageNo 1 \
    --Keyword abc \
    --AllPage True
```

Output: 
```
{
    "Response": {
        "Extra": "abc",
        "Msg": "abc",
        "Data": {
            "List": [
                {
                    "Id": 1,
                    "Logo": "abc",
                    "Name": "abc",
                    "ColorCode": "abc",
                    "CreatedUser": "abc",
                    "CreatedAt": "abc",
                    "MemberCount": 0,
                    "PageCount": 0,
                    "LastModifyName": "abc",
                    "Source": "abc",
                    "Apply": true,
                    "UpdatedUser": "abc",
                    "UpdatedAt": "abc",
                    "CorpId": "abc",
                    "Mark": "abc",
                    "Seed": "abc",
                    "AuthList": [
                        "abc"
                    ],
                    "PanelScope": "abc",
                    "IsExternalManage": true,
                    "ManagePlatform": "abc"
                }
            ],
            "Total": 1,
            "TotalPages": 1
        },
        "RequestId": "abc"
    }
}
```

