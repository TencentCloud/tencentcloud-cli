**Example 1: 获取自定义脚本信息列表**



Input: 

```
tccli bm DescribeUserCmds --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderField createTime \
    --Order 1 \
    --SearchKey 3
```

Output: 
```
{
    "Response": {
        "TotalCount": 8,
        "UserCmds": [
            {
                "AutoId": 87,
                "Alias": "111",
                "CmdId": "cmd-dr3ja3hq",
                "OsType": "linux",
                "Content": "IyEvYmluL2Jhc2gKZm9yIGkgaW4gezEuLjEwMH0KZG8KICAgIGVjaG8gJGkKCXNsZWVwIDEwCmRvbmUK",
                "CreateTime": "2018-05-31 11:57:39",
                "ModifyTime": "2018-06-15 20:12:59",
                "AppId": 123
            },
            {
                "AutoId": 53,
                "Alias": "aa",
                "CmdId": "cmd-o9o03bk8",
                "OsType": "linux",
                "Content": "U1hsRmRtUllUbmxNTWtwd1ltazVkMkZJUVV0UVJEbDNZVWhCUzBOcFVtcGlNMVoxWkVOQk9VbEVRVGREYm1SdllWZDRiRWxEYURCamJsWnNTMUZ3TjBObmEydFpNamt4WW01UmNrdDZjMHREV0U1eldsZFdkMHRFU1hCUGQyOUtXbGRPYjJKNVFXdFpNamt4WW01Uk4wTnVNRDA9",
                "CreateTime": "2017-10-19 16:06:59",
                "ModifyTime": "2017-10-19 16:54:13",
                "AppId": 123
            },
            {
                "AutoId": 28,
                "Alias": "for",
                "CmdId": "cmd-ow3g7elm",
                "OsType": "linux",
                "Content": "Iy9iaW4vYmFzaApjbGVhcgpmb3IgbnVtIGluIDEgMiAzIDQgNSA2IDcgOCA5IDEwCmRvCiAgICBlY2hvICIkbnVtIgpkb25l",
                "CreateTime": "2017-10-12 21:33:00",
                "ModifyTime": "2017-10-12 21:33:00",
                "AppId": 123
            },
            {
                "AutoId": 27,
                "Alias": "比较两数大小",
                "CmdId": "cmd-jvrav3la",
                "OsType": "linux",
                "Content": "Iy9iaW4vYmFzaAplY2hvICJwbGVhc2UgZW50ZXIgdHdvIG51bWJlciIKcmVhZCBhCnJlYWQgYgppZiB0ZXN0ICRhIC1lcSAkYgp0aGVuIGVjaG8gIk5PLjEgPSBOTy4yIgplbGlmIHRlc3QgJGEgLWd0ICRiCnRoZW4gZWNobyAiTk8uMSA+IE5PLjIiCmVsc2UgZWNobyAiTk8uMSA8IE5PLjIiIApmaQ==",
                "CreateTime": "2017-10-12 21:14:56",
                "ModifyTime": "2017-10-12 21:14:56",
                "AppId": 123
            },
            {
                "AutoId": 8,
                "Alias": "1测试",
                "CmdId": "cmd-c33atn9o",
                "OsType": "linux",
                "Content": "dW5hbWVlIC1hIApwd2QKCmxzIFwKLWwKCmVjaG8gJDEK",
                "CreateTime": "2017-10-10 18:38:19",
                "ModifyTime": "2017-10-10 18:49:34",
                "AppId": 123
            }
        ],
        "RequestId": "5fa2a5ff-de11-414d-ae12-f45bf7a87fe4"
    }
}
```

