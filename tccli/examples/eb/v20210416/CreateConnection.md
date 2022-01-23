**Example 1: 创建连接器**



Input: 

```
tccli eb CreateConnection --cli-unfold-argument  \
    --EventBusId eb-l65vlc2 \
    --Type tdmq \
    --ConnectionDescription.ResourceDescription qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1 \
    --ConnectionDescription.APIGWParams None \
    --ConnectionName conn
```

Output: 
```
{
    "Response": {
        "ConnectionId": "connection-5t492ybt",
        "RequestId": "99d8d400-2bde-49d6-99f4-7367907e5964"
    }
}
```

