**Example 1: Agent上报心跳信息**



Input: 

```
tccli bdrc ReportGatewayHeartbeat --cli-unfold-argument  \
    --InstanceId brc-client-a3229ab8-3fba-dcb0-ee21-5bc52c0183cf \
    --AgentIp 172.16.16.2 \
    --AgentSeq 50 \
    --AgentVersion 2.9.20.1 \
    --AutoUpdate enable \
    --CheckUpdate true \
    --CvmInstanceId ins-eej84hs4
```

Output: 
```
{
    "Response": {
        "AppId": 260095320,
        "JobIDs": [],
        "RequestId": "5073ee21-3e7c-4ef5-a2f6-35e229528fa7",
        "SubAccountUin": "700002520084",
        "Uin": "700002520084"
    }
}
```

