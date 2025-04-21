**Example 1: 示例1**



Input: 

```
tccli ioa DescribeSoftCategoryEntry --cli-unfold-argument  \
    --StartIp 192.168.1.1 \
    --OsType 1 \
    --UserId 1 \
    --GroupId 1 \
    --EndIp 192.168.1.10
```

Output: 
```
{
    "Response": {
        "RequestId": "5e022320-c8e7-4001-bced-79c02465db81",
        "Data": {
            "Page": {
                "PageSize": 1000,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Items": [
                {
                    "CategoryId": 10000001,
                    "Name": "未分类",
                    "InstalledDeviceCount": 0,
                    "AuthSoftCount": 0,
                    "InstalledSoftCount": 0,
                    "GenuineRate": 0,
                    "CategoryNamePath": "所有软件.未分类",
                    "CategoryIdPath": "10000000.10000001",
                    "Itime": "",
                    "Utime": "",
                    "CategorySoftCount": 0
                }
            ]
        }
    }
}
```

**Example 2: 查询软件分类列表**



Input: 

```
tccli ioa DescribeSoftCategoryEntry --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "06f8f8bb-ca66-43ee-8d35-26eb3a888666",
        "Data": {
            "Page": {
                "Total": 1,
                "PageCount": 1,
                "PageSize": 1000,
                "PageNum": 1
            },
            "Items": [
                {
                    "CategoryNamePath": "所有软件.未分类",
                    "CategoryIdPath": "1.2",
                    "Itime": "",
                    "Name": "未分类",
                    "CategoryId": 2,
                    "Utime": "",
                    "CategorySoftCount": 10,
                    "InstalledDeviceCount": 2,
                    "AuthSoftCount": 0,
                    "InstalledSoftCount": 10,
                    "GenuineRate": 0
                }
            ]
        }
    }
}
```

