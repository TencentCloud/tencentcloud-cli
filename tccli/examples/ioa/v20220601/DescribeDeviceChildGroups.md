**Example 1: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceChildGroups --cli-unfold-argument  \
    --ParentId 92 \
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
                    "Count": 11,
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
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                },
                {
                    "BindAccount": 1,
                    "Count": 11,
                    "Description": "",
                    "FromAuto": 0,
                    "HasIp": false,
                    "Icon": "",
                    "Id": 74699,
                    "IdPath": "92.74699",
                    "IsLeaf": false,
                    "Locked": 2,
                    "Name": "Test-New",
                    "NamePath": "全网终端.Test-New",
                    "OsType": 0,
                    "ParentId": 92,
                    "ReadOnly": false,
                    "Sort": 0,
                    "WithIp": 0
                }
            ]
        },
        "RequestId": "73d262a9-4c0f-4f68-bce2-3718f98c6494"
    }
}
```

