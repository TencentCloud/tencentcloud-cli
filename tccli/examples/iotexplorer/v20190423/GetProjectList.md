**Example 1: 查询项目列表**

当用户在自己的业务系统中想进行产品管理时，可以通过查询项目列表接口查询用户在物联网开发平台创建的项目。

Input: 

```
tccli iotexplorer GetProjectList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Projects": [
            {
                "ProjectId": "prj-cmz8cu77",
                "ProjectName": "CreatePrj",
                "ProjectDesc": "BBBBB",
                "CreateTime": 1560328009,
                "UpdateTime": 1560328009,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-k1c2y9n6",
                "ProjectName": "Name",
                "ProjectDesc": "Desc",
                "CreateTime": 1560322591,
                "UpdateTime": 1560322591,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-qwdtv1p2",
                "ProjectName": "PName",
                "ProjectDesc": "prjDesc",
                "CreateTime": 1560311336,
                "UpdateTime": 1560311336,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-v6j6xbq9",
                "ProjectName": "prjName",
                "ProjectDesc": "prjDesc",
                "CreateTime": 1560310472,
                "UpdateTime": 1560310472,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-4r2kajtp",
                "ProjectName": "字符串",
                "ProjectDesc": "字符串",
                "CreateTime": 1557459725,
                "UpdateTime": 1559743207,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-zunfat46",
                "ProjectName": "abcde229环境",
                "ProjectDesc": "desc",
                "CreateTime": 1556250427,
                "UpdateTime": 1559743210,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-9z3jg93n",
                "ProjectName": "test229环境",
                "ProjectDesc": "afdafd",
                "CreateTime": 1556248181,
                "UpdateTime": 1559743210,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-zycc6aau",
                "ProjectName": "字符串229环境",
                "ProjectDesc": "字符串",
                "CreateTime": 1556245194,
                "UpdateTime": 1559743210,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            },
            {
                "ProjectId": "prj-3u6jqd4m",
                "ProjectName": "name1229环境",
                "ProjectDesc": "desc1",
                "CreateTime": 1556199700,
                "UpdateTime": 1559743211,
                "ProductCount": 0,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "DeviceCount": 0,
                "ApplicationCount": 0
            }
        ],
        "RequestId": "9dbce8ec-76e2-4f34-8c32-ad548b3b598a",
        "Total": 9
    }
}
```

