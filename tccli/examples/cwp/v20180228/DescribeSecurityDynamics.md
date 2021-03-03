**Example 1: 获取安全事件消息数据**

获取安全事件消息数据。

Input: 

```
tccli cwp DescribeSecurityDynamics --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityDynamics": [
            {
                "Uuid": "add4a78a-0d59-11e8-b7ab-00e081e1a5c5",
                "EventTime": "2018-10-08 12:12:22",
                "EventType": "MALWARE",
                "Message": "发现主机10.10.10.12存在恶意文件5个",
                "SecurityLevel": "xx"
            }
        ],
        "TotalCount": 100
    }
}
```

