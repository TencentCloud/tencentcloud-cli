**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDeviceGroup --cli-unfold-argument  \
    --Id 42631
```

Output: 
```
{
    "Response": {
        "RequestId": "1f9563e3-556c-46a6-ac6b-16dd9c96eccc",
        "Data": {
            "Sort": 1,
            "OsType": 0,
            "IdPath": "42631",
            "Id": 42631,
            "IpList": [],
            "Description": "",
            "FromAuto": 0,
            "Name": "全网终端",
            "NamePath": "全网终端",
            "ParentId": 0,
            "Locked": 0
        }
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceGroup --cli-unfold-argument  \
    --Id 92
```

Output: 
```
{
    "Response": {
        "Data": {
            "Description": "",
            "FromAuto": 0,
            "Id": 0,
            "IdPath": "",
            "IpList": [],
            "Locked": 0,
            "Name": "",
            "NamePath": "",
            "OsType": 0,
            "ParentId": 0,
            "Sort": 0
        },
        "RequestId": "42c56b2f-d5c7-46ba-96e0-8adbb27e527b"
    }
}
```

