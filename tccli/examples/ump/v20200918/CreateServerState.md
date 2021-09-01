**Example 1: 服务器监控信息**



Input: 

```
tccli ump CreateServerState --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --ReportTime 123456789 \
    --ServerStateItems.0.ServerState 1 \
    --ServerStateItems.0.ServerIp 192.168.1.1 \
    --ServerStateItems.0.DiskInfos.0.DiskName /dev/sdb \
    --ServerStateItems.0.DiskInfos.0.Usage 0.45
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

