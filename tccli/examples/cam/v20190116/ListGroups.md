**Example 1: 查询用户组列表**



Input: 

```
tccli cam ListGroups --cli-unfold-argument  \
    --Page 1 \
    --Rp 20
```

Output: 
```
{
    "Response": {
        "TotalNum": 2,
        "GroupInfo": [
            {
                "GroupId": 2021,
                "GroupName": "test2",
                "CreateTime": "2019-04-03 15:15:18",
                "Remark": "test2"
            },
            {
                "GroupId": 2020,
                "GroupName": "test1",
                "CreateTime": "2019-04-03 15:11:34",
                "Remark": "test2"
            }
        ],
        "RequestId": "dbb91d87-5e3f-42b4-8cc9-ad9f16600370"
    }
}
```

