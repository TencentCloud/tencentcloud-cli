**Example 1: 获取主题下绑定的域名列表**



Input: 

```
tccli cdn ListClsTopicDomains --cli-unfold-argument  \
    --TopicId d2256449-c6ff-421b-93ef-aa3a7dde2de2 \
    --LogsetId 6d04373b-ba59-4a4f-a96e-9fe53b59a536 \
    --Channel cdn
```

Output: 
```
{
    "Response": {
        "TopicId": "d2256449-c6ff-421b-93ef-aa3a7dde2de2",
        "UpdateTime": "2020-09-22 00:00:00",
        "TopicName": "test",
        "DomainAreaConfigs": [
            {
                "Domain": "a.b.com",
                "Area": [
                    "mainland"
                ]
            }
        ],
        "RequestId": "57460798-8723-45e3-9c75-a0599ef9143a",
        "AppId": 12345678901,
        "LogsetId": "6d04373b-ba59-4a4f-a96e-9fe53b59a536",
        "Channel": "cdn"
    }
}
```

