**Example 1: 获取应用下程序包列表**

获取应用application-jy9w6lka下的程序包信息

Input: 

```
tccli tsf DescribePkgs --cli-unfold-argument  \
    --ApplicationId application-xxxxxxxx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "PkgId": "xx",
                    "PkgType": "xx",
                    "UploadTime": "xx",
                    "PkgName": "xx",
                    "PkgDesc": "xx",
                    "PkgBindInfo": [
                        {
                            "ApplicationId": "xx",
                            "GroupId": "xx"
                        }
                    ],
                    "PkgVersion": "xx",
                    "PkgPubStatus": 1,
                    "Md5": "xx"
                },
                {
                    "PkgId": "xx",
                    "PkgType": "xx",
                    "UploadTime": "xx",
                    "PkgName": "xx",
                    "PkgDesc": "xx",
                    "PkgBindInfo": [
                        {
                            "ApplicationId": "xx",
                            "GroupId": "xx"
                        }
                    ],
                    "PkgVersion": "xx",
                    "PkgPubStatus": 1,
                    "Md5": "xx"
                }
            ],
            "TotalCount": 2,
            "RepositoryType": "xx",
            "RepositoryName": "xx",
            "RepositoryId": "xx"
        },
        "RequestId": "xx"
    }
}
```

