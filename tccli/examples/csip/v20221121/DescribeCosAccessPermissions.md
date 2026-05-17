**Example 1: 查看对象存储访问权限列表**



Input: 

```
tccli csip DescribeCosAccessPermissions --cli-unfold-argument  \
    --RelAppId 183479120 \
    --BucketName brain-183479120
```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e",
        "Data": [
            {
                "AccessUin": "100000000001",
                "NickName": "测试用户",
                "Identity": 1,
                "MainNickName": "主账号用户",
                "AkList": [
                    "AKID1234567890abcdef,AKID0987654321fedcba"
                ],
                "CamPolicyCount": 3,
                "UpdateTime": 1705293000
            },
            {
                "AccessUin": "100000000002",
                "NickName": "生产用户",
                "Identity": 2,
                "MainNickName": "主账号用户",
                "AkList": [
                    "AKIDabcdef1234567890"
                ],
                "CamPolicyCount": 1,
                "UpdateTime": 1705296000
            },
            {
                "AccessUin": "100000000003",
                "NickName": "子账号用户",
                "Identity": 3,
                "MainNickName": "主账号用户",
                "AkList": [
                    "AKIDfedcba0987654321"
                ],
                "CamPolicyCount": 2,
                "UpdateTime": 1705299000
            }
        ],
        "Total": 3
    }
}
```

