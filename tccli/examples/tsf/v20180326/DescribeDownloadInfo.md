**Example 1: 获取下载程序包信息**

获取应用application-zxxxxxxx下程序包id为pkg-xxxxxxx的下载信息

Input: 

```
tccli tsf DescribeDownloadInfo --cli-unfold-argument  \
    --ApplicationId application-zxxxxxxx \
    --PkgId pkg-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "2e9885d9-xxxx-xxxx-xxxx-59621dd82a5b",
        "Result": {
            "Bucket": "tsf-gz-123456789",
            "Region": "ap-guangzhou",
            "Path": "/1111111111/application-xxxxxxxx/201905291xxxxx/travel-passenger-xxx-1.0-SNAPSHOT.jar",
            "Credentials": {
                "SessionToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "TmpAppId": "123456789",
                "TmpSecretId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "TmpSecretKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "ExpiredTime": 1559120000,
                "Domain": "cos.ap-guangzhou.myqcloud.com"
            }
        }
    }
}
```

