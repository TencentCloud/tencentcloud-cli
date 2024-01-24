**Example 1: 创建开发空间版本**

创建开发空间版本

Input: 

```
tccli wedata CreateFileVersion --cli-unfold-argument  \
    --ResourceId abc \
    --CreateTime abc \
    --Description abc \
    --TaskId abc \
    --TaskVersionNum abc \
    --TaskVersionId abc \
    --UserName abc \
    --ProjectId abc \
    --RemotePath abc \
    --ObjectRegion abc \
    --ObjectBucketName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

