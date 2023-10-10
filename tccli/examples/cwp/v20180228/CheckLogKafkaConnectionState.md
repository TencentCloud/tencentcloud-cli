**Example 1: 检查日志投递kafka连通性**



Input: 

```
tccli cwp CheckLogKafkaConnectionState --cli-unfold-argument  \
    --AccessType 1 \
    --AccessAddr 192.168.1.1:80 \
    --Username xx \
    --HasPwd 1 \
    --Pwd xxxx \
    --KafkaId ckafka-ce80kte5 \
    --InsVersion 0.10.2.1
```

Output: 
```
{
    "Response": {
        "RequestId": "bf93077b-51f5-4428-b9de-7e33a0b9cc4a",
        "IsConnect": true
    }
}
```

