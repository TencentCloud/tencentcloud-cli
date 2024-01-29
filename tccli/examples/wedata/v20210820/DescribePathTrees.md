**Example 1: 开发空间-拉取完整目录树请求体**

开发空间-拉取完整目录树请求体

Input: 

```
tccli wedata DescribePathTrees --cli-unfold-argument  \
    --ProjectId 1486804694126882816
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "abc",
                "Title": "abc",
                "Type": "abc",
                "ParentId": "abc",
                "IsLeaf": true,
                "Params": {
                    "LocalPath": "abc",
                    "RemotePath": "abc",
                    "ResourceId": "abc",
                    "UpdateTime": 0,
                    "UpdateUserId": "abc",
                    "FileExtensionType": "abc",
                    "UpdateUser": "abc"
                },
                "Children": [
                    {
                        "Id": "abc",
                        "Title": "abc",
                        "Type": "abc",
                        "ParentId": "abc",
                        "IsLeaf": true,
                        "Params": {
                            "LocalPath": "abc",
                            "RemotePath": "abc",
                            "ResourceId": "abc",
                            "UpdateTime": 0,
                            "UpdateUserId": "abc",
                            "FileExtensionType": "abc",
                            "UpdateUser": "abc"
                        },
                        "Children": [
                            {
                                "Id": "abc",
                                "Title": "abc",
                                "Type": "abc",
                                "ParentId": "abc",
                                "IsLeaf": true,
                                "Params": {
                                    "LocalPath": "abc",
                                    "RemotePath": "abc",
                                    "ResourceId": "abc",
                                    "UpdateTime": 0,
                                    "UpdateUserId": "abc",
                                    "FileExtensionType": "abc",
                                    "UpdateUser": "abc"
                                }
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

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata DescribePathTrees --cli-unfold-argument  \
    --ProjectId 1567736773494575104
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "428a7890-668b-411b-93cd-4144e0fe29fc"
    }
}
```

**Example 3: 错误示例-2**

错误示例-2

Input: 

```
tccli wedata DescribePathTrees --cli-unfold-argument  \
    --ProjectId 1567736773494575104
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "c5bd3e43-bc29-4e5d-947d-49e6c3d7ca8d"
    }
}
```

