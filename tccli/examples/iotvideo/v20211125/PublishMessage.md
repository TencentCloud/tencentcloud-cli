**Example 1: 透传Payload至设备**



Input: 

```
tccli iotvideo PublishMessage --cli-unfold-argument  \
    --Topic RL0BAZKZ6V/dev1/control \
    --Payload AASDFASFSADFASDF \
    --ProductId Nlasdf****ABCd \
    --DeviceName dev1 \
    --Qos 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

