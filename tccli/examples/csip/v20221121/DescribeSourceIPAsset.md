**Example 1: 获取用户访问密钥资产列表**



Input: 

```
tccli csip DescribeSourceIPAsset --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AKInfo": [
                    {
                        "ID": 10079,
                        "Name": "AKID******",
                        "Remark": "",
                        "User": "name"
                    },
                    {
                        "ID": 10086,
                        "Name": "AKID******",
                        "Remark": "",
                        "User": "name"
                    },
                    {
                        "ID": 10093,
                        "Name": "临时密钥",
                        "Remark": "临时密钥",
                        "User": "name"
                    }
                ],
                "AccessKeyAlarmList": [
                    {
                        "Count": 4,
                        "Type": 0
                    }
                ],
                "ActionCount": 145,
                "AppID": 1200001,
                "EventType": 1,
                "ID": 10009,
                "IPType": 1,
                "InstanceID": "",
                "InstanceName": "",
                "LastAccessTime": "2025-03-13 16:39:00",
                "Nickname": "name",
                "Region": "中国 广东省 广州市",
                "Remark": "",
                "SourceIP": "106.55.200.***",
                "Uin": "1000001"
            }
        ],
        "RequestId": "e9780808-1e10-4a63-bd2b-dbd74264091a",
        "Total": 2
    }
}
```

