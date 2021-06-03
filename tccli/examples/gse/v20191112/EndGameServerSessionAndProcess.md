**Example 1: 终止游戏服务器会话的进程**



Input: 

```
tccli gse EndGameServerSessionAndProcess --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-pxxx/xxx \
    --IpAddress 0.0.0.0 \
    --Port 8888
```

Output: 
```
{
    "Response": {
        "RequestId": "84708eb1-0247-43f8-834e-c7edfdsfdgd53"
    }
}
```

