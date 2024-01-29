**Example 1: 脚本回收站目录树**

脚本回收站目录树

Input: 

```
tccli wedata GetPathTrees --cli-unfold-argument  \
    --ProjectId abc \
    --Keyword abc \
    --Script True \
    --PageNumber 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 0,
            "PageSize": 0,
            "Rows": [
                {
                    "ResourceId": "abc",
                    "FileName": "abc",
                    "FileExtensionType": "abc",
                    "Type": "abc",
                    "Md5Value": "abc",
                    "CreateTime": "abc",
                    "UpdateTime": "abc",
                    "Size": 1,
                    "LocalPath": "abc",
                    "RemotePath": "abc",
                    "OwnerName": "abc",
                    "Owner": "abc",
                    "PathDepth": 1,
                    "ProjectId": "abc",
                    "ExtraInfo": "abc",
                    "LocalTempPath": "abc",
                    "ZipPath": "abc",
                    "Bucket": "abc",
                    "Region": "abc",
                    "DeleteName": "abc",
                    "DeleteOwner": "abc",
                    "Operator": "abc",
                    "OperatorName": "abc"
                }
            ],
            "TotalCount": 0,
            "TotalPageNumber": 0
        },
        "RequestId": "abc"
    }
}
```

