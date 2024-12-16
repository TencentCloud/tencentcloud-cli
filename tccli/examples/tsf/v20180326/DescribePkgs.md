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
                    "PkgId": "pkg-6a79x94v",
                    "PkgName": "java-consumer",
                    "PkgType": "jar",
                    "PkgVersion": "v1",
                    "PkgDesc": "this is a desc",
                    "UploadTime": "2020-11-12 09:12:33",
                    "Md5": "2s78294s810xxxxxxxxxxx",
                    "PkgPubStatus": 0,
                    "PkgBindInfo": [
                        {
                            "ApplicationId": "application-6a79x94v",
                            "GroupId": "group-6a79x94v"
                        }
                    ]
                }
            ],
            "RepositoryId": "repository-6a79x94v",
            "RepositoryType": "cos",
            "RepositoryName": "bucket-mock"
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

