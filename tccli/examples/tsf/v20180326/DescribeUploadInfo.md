**Example 1: 获取上传程序包信息**



Input: 

```
tccli tsf DescribeUploadInfo --cli-unfold-argument  \
    --PkgName test-drvier-api-1.0.0-SNAPSHOT.jar \
    --PkgType fatjar \
    --PkgVersion 20190529xxxxxx \
    --ApplicationId application-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "7b3c781d-xxxx-47d4-xxxx-807a73291ff7",
        "Result": {
            "PkgId": "pkg-zzzzzz",
            "Bucket": "tsf-gz-123456789",
            "Region": "ap-guangzhou",
            "Path": "111111111/application-xxxxxxxx/20190529174449/test.jar",
            "Credentials": {
                "SessionToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "TmpAppId": "123456789",
                "TmpSecretId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "TmpSecretKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "ExpiredTime": 1559100000,
                "Domain": "cos.ap-guangzhou.myqcloud.com"
            }
        }
    }
}
```

