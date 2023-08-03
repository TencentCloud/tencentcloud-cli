**Example 1: 获取Kakfa协议消费信息**



Input: 

```
tccli cls DescribeKafkaConsumer --cli-unfold-argument  \
    --FromTopicId a5ce0c9c-0690-44a5-bc79-5f2190626bd0
```

Output: 
```
{
    "Response": {
        "Status": true,
        "TopicID": "125407-ad2155c6-XXXX-45b5-83c9-8b42b6f59fbd",
        "Compression": 2,
        "ConsumerContent": {
            "Format": 1,
            "MetaFields": [
                "__SOURCE__",
                "__FILENAME__",
                "__TIMESTAMP__",
                "__HOSTNAME__",
                "__PKGID__"
            ],
            "EnableTag": true,
            "JsonType": 1,
            "TagTransaction": 1
        },
        "RequestId": "ddfdXXX-4ef3-43fd-b1cf-4f4a0b944d26"
    }
}
```

