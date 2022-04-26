**Example 1: 发布消息**



Input: 

```
tccli iotcloud PublishMessage --cli-unfold-argument  \
    --Topic RL0BAZKZ6V/dev1/control \
    --Payload hahaha \
    --ProductId RL0BAZKZ6V \
    --DeviceName dev1 \
    --Qos 0
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

