**Example 1: 客户端没有遗嘱消息**

当前查询的客户端没有遗嘱消息

Input: 

```
tccli mqtt DescribeWillMessage --cli-unfold-argument  \
    --InstanceId mqtt-mwe5jvvr \
    --ClientId client1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "f7ab1f26-b6d6-4a75-9909-36fad448e3c3"
    }
}
```

**Example 2: 示例**

示例

Input: 

```
tccli mqtt DescribeWillMessage --cli-unfold-argument  \
    --InstanceId mqtt-mwe5jvvr \
    --ClientId test_device_custom_791394
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ContentType": "application/json",
        "CorrelationData": "MTIz",
        "CreateTime": 1764918589000,
        "MessageExpiryInterval": 100,
        "Payload": "dGhpcyBpcyB3aWxsIG1lc3NhZ2U=",
        "PayloadFormatIndicator": 1,
        "Qos": 1,
        "RequestId": "30aa2d8e-433b-441b-8350-9d06d72eafdc",
        "ResponseTopic": "/home/resp/1",
        "Retained": true,
        "Topic": "home/will",
        "UpdateTime": 1764918589720,
        "WillDelayInterval": 0
    }
}
```

