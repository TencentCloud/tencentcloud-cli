**Example 1: 数据开发-获取资源目录树**

获取资源路径列表

Input: 

```
tccli wedata GetResourcePathTree --cli-unfold-argument  \
    --ProjectId abc \
    --Name abc \
    --FileType abc \
    --FilePath abc \
    --DirectoryType abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Name": "abc",
                "IsLeaf": true,
                "ResourceId": "abc",
                "LocalPath": "abc",
                "RemotePath": "abc",
                "FileExtensionType": "abc",
                "Size": 0,
                "MD5Value": "abc",
                "OwnerName": "abc",
                "UpdateUser": "abc",
                "UpdateUserId": "abc",
                "CreateTime": 0,
                "UpdateTime": 0,
                "Bucket": "abc",
                "Region": "abc",
                "ExtraInfo": "abc",
                "Children": [
                    {
                        "Name": "abc",
                        "IsLeaf": true,
                        "ResourceId": "abc",
                        "LocalPath": "abc",
                        "RemotePath": "abc",
                        "FileExtensionType": "abc",
                        "Size": 0,
                        "MD5Value": "abc",
                        "OwnerName": "abc",
                        "UpdateUser": "abc",
                        "UpdateUserId": "abc",
                        "CreateTime": 0,
                        "UpdateTime": 0,
                        "Bucket": "abc",
                        "Region": "abc",
                        "ExtraInfo": "abc",
                        "Children": [
                            {
                                "Name": "abc",
                                "IsLeaf": true,
                                "ResourceId": "abc",
                                "LocalPath": "abc",
                                "RemotePath": "abc",
                                "FileExtensionType": "abc",
                                "Size": 0,
                                "MD5Value": "abc",
                                "OwnerName": "abc",
                                "UpdateUser": "abc",
                                "UpdateUserId": "abc",
                                "CreateTime": 0,
                                "UpdateTime": 0,
                                "Bucket": "abc",
                                "Region": "abc",
                                "ExtraInfo": "abc"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

