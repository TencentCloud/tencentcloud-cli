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
        "RequestId": "28b080e7-xxxx-xxxx-xxxx-ba8ea7f50be3",
        "Result": {
            "Content": [
                {
                    "PkgId": "pkg-xxxxxxxx",
                    "PkgName": "test-1.0.0-SNAPSHOT.jar",
                    "PkgType": "fatjar",
                    "PkgVersion": "20190529xxxxxx",
                    "PkgDesc": "",
                    "UploadTime": "2019-05-29 15:xx:xx",
                    "Md5": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "PkgPubStatus": 1
                },
                {
                    "PkgId": "pkg-xxxxxxxx",
                    "PkgName": "test1-1.0.0-SNAPSHOT.jar",
                    "PkgType": "fatjar",
                    "PkgVersion": "20190529xxxxxx",
                    "PkgDesc": "",
                    "UploadTime": "2019-05-29 13:xx:xx",
                    "Md5": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "PkgPubStatus": 1
                }
            ],
            "TotalCount": 2
        }
    }
}
```

