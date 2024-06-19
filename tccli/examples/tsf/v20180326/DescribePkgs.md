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
            "TotalCount": 0,
            "Content": [
                {
                    "PkgId": "abc",
                    "PkgName": "abc",
                    "PkgType": "abc",
                    "PkgVersion": "abc",
                    "PkgDesc": "abc",
                    "UploadTime": "abc",
                    "Md5": "abc",
                    "PkgPubStatus": 0,
                    "PkgBindInfo": [
                        {
                            "ApplicationId": "abc",
                            "GroupId": "abc"
                        }
                    ]
                }
            ],
            "RepositoryId": "abc",
            "RepositoryType": "abc",
            "RepositoryName": "abc"
        },
        "RequestId": "abc"
    }
}
```

