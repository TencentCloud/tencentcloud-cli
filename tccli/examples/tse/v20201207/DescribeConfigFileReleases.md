**Example 1: 获取版本发布列表**

获取版本发布列表

Input: 

```
tccli tse DescribeConfigFileReleases --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Group abc \
    --FileName abc \
    --OnlyUse True \
    --ReleaseName abc \
    --OrderField abc \
    --OrderDesc abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Releases": [
            {
                "Id": 1,
                "Name": "abc",
                "Namespace": "abc",
                "Group": "abc",
                "FileName": "abc",
                "Content": "abc",
                "Comment": "abc",
                "Md5": "abc",
                "Version": 1,
                "CreateTime": "abc",
                "CreateBy": "abc",
                "ModifyTime": "abc",
                "ModifyBy": "abc",
                "ReleaseDescription": "abc",
                "Active": true,
                "Format": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

