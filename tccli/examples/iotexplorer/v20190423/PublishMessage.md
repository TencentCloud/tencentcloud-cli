**Example 1: 透传Payload至设备**



Input: 

```
tccli iotexplorer PublishMessage --cli-unfold-argument  \
    --Topic J2CRPPZ8J4/dev1/control \
    --Payload AASDFASFSADFASDF \
    --ProductId J2CRPPZ8J4 \
    --DeviceName dev1 \
    --Qos 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4e97e"
    }
}
```

**Example 2: 将接收到的经过业务系统base64编码后的Payload进行二进制编码后下发至设备**



Input: 

```
tccli iotexplorer PublishMessage --cli-unfold-argument  \
    --ProductId J2CRPPZ8J4 \
    --DeviceName test01 \
    --Topic J2CRPPZ8J4/test01/data \
    --Payload 5L2g5aW977yM5LiW55WM44CC \
    --PayloadEncoding base64
```

Output: 
```
{
    "Response": {
        "RequestId": "keyixie_b4f3cb87-2224-46b2-ac2c-e28feadb61c8"
    }
}
```

