**Example 1: 开发空间-拉取指定路径目录树**

开发空间-拉取指定路径目录树

Input: 

```
tccli wedata DescribeChildrenPathTrees --cli-unfold-argument  \
    --ProjectId abc \
    --LocalPath abc \
    --IncludeFile abc \
    --QueryDepth 0
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 开发空间-拉取指定路径目录树（包含文件）**

开发空间-拉取指定路径目录树（包含文件）

Input: 

```
tccli wedata DescribeChildrenPathTrees --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --LocalPath /datastudio/project/FusionTest \
    --IncludeFile true \
    --QueryDepth 2
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeChildrenPathTrees --cli-unfold-argument  \
    --ProjectId 1567736773494575104 \
    --LocalPath /datastudio/project/zheyuwang \
    --IncludeFile true \
    --QueryDepth 3
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "6ce02774-d244-4780-8755-00e6df991a3f"
    }
}
```

