**Example 1: 查看站点列表的验证信息列表**

查看已经添加的站点的验证信息列表

Input: 

```
tccli cws DescribeSitesVerification --cli-unfold-argument  \
    --Urls http%3A%2F%2Fwww.qcloud.com
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SitesVerification": [
            {
                "Appid": 1251001047,
                "CreatedAt": "2018-03-19T16:07:57+08:00",
                "Domain": "qq.com",
                "Id": 1,
                "TxtName": "verify-wcpfql",
                "TxtText": "vps9iq4hmn7suiad7v8sn9isawn5yteh",
                "UpdatedAt": "2018-03-23T00:02:11+08:00",
                "ValidTo": "2018-04-18T16:07:57+08:00",
                "VerifyStatus": 1
            }
        ],
        "TotalCount": 1
    }
}
```

