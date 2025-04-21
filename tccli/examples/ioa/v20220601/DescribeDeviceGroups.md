**Example 1: 查询分组信息**



Input: 

```
tccli ioa DescribeDeviceGroups --cli-unfold-argument  \
    --OsType 0 \
    --ParentId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3e7cdb3a-f729-4ace-86c5-0f478591d0ad",
        "Data": {
            "Page": {
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1000,
                "PageNum": 1
            },
            "Items": null
        }
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceGroups --cli-unfold-argument  \
    --ParentId 0 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BindAccount": 0,
                    "Count": 1,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 74699,
                    "IdPath": "92.74699",
                    "IsLeaf": true,
                    "Locked": 2,
                    "Name": "Test-New",
                    "NamePath": "全网终端.Test-New",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 0,
                    "Count": 4,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 74700,
                    "IdPath": "92.74700",
                    "IsLeaf": false,
                    "Locked": 2,
                    "Name": "TestBone",
                    "NamePath": "全网终端.TestBone",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 0,
                    "Count": 1,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 74701,
                    "IdPath": "92.74700.74701",
                    "IsLeaf": true,
                    "Locked": 2,
                    "Name": "BoneLeaf",
                    "NamePath": "全网终端.TestBone.BoneLeaf",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 74700,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 0,
                    "Count": 26,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 92,
                    "IdPath": "92",
                    "IsLeaf": false,
                    "Locked": 0,
                    "Name": "全网终端",
                    "NamePath": "全网终端",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 0,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 0,
                    "Count": 21,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 93,
                    "IdPath": "92.93",
                    "IsLeaf": true,
                    "Locked": 0,
                    "Name": "未分组终端",
                    "NamePath": "全网终端.未分组终端",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 0,
                    "Count": 0,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 94,
                    "IdPath": "92.94",
                    "IsLeaf": true,
                    "Locked": 0,
                    "Name": "服务器",
                    "NamePath": "全网终端.服务器",
                    "OrgId": 0,
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 1000,
                "Total": 6
            }
        },
        "RequestId": "c0943a93-1c1f-4ef0-a506-185fa81e0d5e"
    }
}
```

