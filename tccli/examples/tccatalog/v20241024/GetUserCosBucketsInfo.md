**Example 1: GetUserCosBucketsInfo调用实例**



Input: 

```
tccli tccatalog GetUserCosBucketsInfo --cli-unfold-argument  \
    --UsedFor volume
```

Output: 
```
{
    "Response": {
        "BucketsInfo": [
            {
                "BucketName": "dlc38a3-700002237358-1767681051-700002274418-251440277",
                "BucketStatus": "bind",
                "CreateTime": 1767681051,
                "Description": "used_for_tclake_lakehouse",
                "EntrustAccountUin": "700002274418",
                "ModifyTime": 1767681109,
                "NameSpace": "lakehouse",
                "ProjectId": "tclake",
                "Region": "ap-guangzhou",
                "Summary": "",
                "UserAppId": "260076791",
                "UserUin": "700002237358"
            }
        ],
        "RequestId": "29e71a1b-d164-4f8f-9428-b4293306c5d1"
    }
}
```

