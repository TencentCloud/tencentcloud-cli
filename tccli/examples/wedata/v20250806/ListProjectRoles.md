**Example 1: 成功调用**



Input: 

```
tccli wedata ListProjectRoles --cli-unfold-argument  \
    --ProjectId 2917360018413740032
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Description": "u9879u76eeu7ba1u7406u5458u4e3bu8981u8d1fu8d23u9879u76eeu65e5u5e38u7ba1u7406uff0cu5177u6709u9879u76eeu5185u7684u6240u6709u6743u9650u3002",
                    "RoleDisplayName": "u9879u76eeu7ba1u7406u5458",
                    "RoleId": "308335260274237440",
                    "RoleName": "ProjectManager"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 5,
            "TotalPageNumber": 1
        },
        "RequestId": "76f96c85-6c67-4c7f-871e-15e5d87007f2"
    }
}
```

