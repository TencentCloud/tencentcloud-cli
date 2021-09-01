**Example 1: 修改告警接收人**



Input: 

```
tccli monitor ModifyAlarmReceivers --cli-unfold-argument  \
    --Module monitor \
    --GroupId 111111 \
    --ReceiverInfos.0.StartTime 61261 \
    --ReceiverInfos.0.EndTime 57599 \
    --ReceiverInfos.0.NotifyWay EMAIL SMS \
    --ReceiverInfos.0.ReceiverType group \
    --ReceiverInfos.0.ReceiverGroupList 118074
```

Output: 
```
{
    "Response": {
        "RequestId": "811066c4-2c19-49aa-8077-9a85006c2ae6"
    }
}
```

