**Example 1: Getting the list of domain names bound to topic**



Input: 

```
tccli cdn ListClsTopicDomains --cli-unfold-argument  \
    --Channel cdn \
    --LogsetId 6d04373b-ba59-4a4f-a96e-9fe53b59a536 \
    --TopicId d2256449-c6ff-421b-93ef-aa3a7dde2de2
```

Output: 
```
{
    "Response": {
        "RequestId": "57460798-8723-45e3-9c75-a0599ef9143a",
        "AppId": 12345678901,
        "Channel": "cdn",
        "LogsetId": "6d04373b-ba59-4a4f-a96e-9fe53b59a536",
        "TopicId": "d2256449-c6ff-421b-93ef-aa3a7dde2de2",
        "DomainAreaConfigs": [
            {
                "Domain": "a.b.com",
                "Area": [
                    "mainland"
                ]
            }
        ]
    }
}
```

