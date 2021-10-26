**Example 1: 获取指定分类和状态的漏洞列表**

获取指定分类和状态的漏洞列表数据

Input: 

```
tccli cwp DescribeVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "TotalCount": 2,
        "FollowVulCount": 0,
        "VulInfoList": [
            {
                "Ids": "1748",
                "Name": "Linux帐户口令生存期策略",
                "Status": 0,
                "VulId": 100392,
                "PublishTime": "2019-09-02 00:00:00",
                "LastTime": "2020-06-29 03:04:15",
                "HostCount": 1,
                "Level": 2,
                "From": 0,
                "Descript": "口令老化（Password aging）是一种增强的系统口令生命期认证机制，能够确保用户的口令定期更换，提高系统安全性。",
                "PublishTimeWisteria": "",
                "NameWisteria": "",
                "DescriptWisteria": ""
            }
        ]
    }
}
```

