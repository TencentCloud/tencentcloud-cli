**Example 1: 查询分组信息**



Input: 

```
tccli ioa DescribeGroupDevices --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 92
```

Output: 
```
{
    "Response": {
        "RequestId": "cc61d0b6-85e6-4a88-9836-2b6aa90b6ad1",
        "Data": {
            "Page": {
                "Total": 1,
                "PageCount": 0,
                "PageSize": 0,
                "PageNum": 0
            },
            "Items": [
                {
                    "Mid": "60A79588CD1400107221E490335AA1BA63730928",
                    "GroupId": 93,
                    "Locked": 2,
                    "GroupName": "未分组终端",
                    "Mac": "00:0C:29:4A:67:9E",
                    "Name": "DESKTOP-6G9TH91",
                    "Ip": "119.147.10.206",
                    "Id": 20
                }
            ]
        }
    }
}
```

