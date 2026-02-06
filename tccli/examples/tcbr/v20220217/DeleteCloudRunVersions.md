**Example 1: 批量删除版本**



Input: 

```
tccli tcbr DeleteCloudRunVersions --cli-unfold-argument  \
    --EnvId abc \
    --IsDeleteServer True \
    --IsDeleteImage True \
    --OperatorRemark abc \
    --SimpleVersions.0.EnvId abc \
    --SimpleVersions.0.ServerName abc \
    --SimpleVersions.0.VersionName abc
```

Output: 
```
{
    "Response": {
        "Result": "abc",
        "FailVersions": [
            {
                "Version": {
                    "EnvId": "abc",
                    "ServerName": "abc",
                    "VersionName": "abc"
                },
                "ErrorCode": 0,
                "ErrorMsg": "abc",
                "RequestId": "abc"
            }
        ],
        "SuccessVersions": [
            {
                "Version": {
                    "EnvId": "abc",
                    "ServerName": "abc",
                    "VersionName": "abc"
                },
                "RequestId": "abc",
                "Result": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

