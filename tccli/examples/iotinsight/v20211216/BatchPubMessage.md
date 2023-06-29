**Example 1: API数据源接口**



Input: 

```
tccli iotinsight BatchPubMessage --cli-unfold-argument  \
    --SourceId 865618bf-85ba-42da-89a2-613764820aa7 \
    --Messages.0.MessageId 1234 \
    --Messages.0.Payload {"test":"1111"} \
    --Messages.1.MessageId 34567 \
    --Messages.1.Payload {"test":"2222"}
```

Output: 
```
{
    "Response": {
        "RequestId": "eb6dabbc-ee60-453c-956b-45acc018793c"
    }
}
```

