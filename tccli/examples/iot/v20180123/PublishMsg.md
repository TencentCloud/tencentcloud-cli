**Example 1: 向Topic发布消息**

向Topic发布消息，用于从云端向设备端发送消息。

Input: 

```
tccli iot PublishMsg --cli-unfold-argument  \
    --Topic iot-0827lh7q/device1/test \
    --Message test_message \
    --Qos 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a1eec593-a887-49be-8b30-9a80e4a993c7"
    }
}
```

