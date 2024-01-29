**Example 1: 导出项目参数**

导出项目参数

Input: 

```
tccli wedata ExportProjectParamDs --cli-unfold-argument  \
    --ProjectId abc \
    --OriginDomain abc \
    --Range abc \
    --PublishTime abc \
    --Params abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "CosPath": "abc",
            "CosBucketName": "abc",
            "Region": "abc",
            "Token": "abc",
            "SecretId": "abc",
            "SecretKey": "abc",
            "CreateTime": 0,
            "ExpiredTime": 0
        },
        "RequestId": "abc"
    }
}
```

