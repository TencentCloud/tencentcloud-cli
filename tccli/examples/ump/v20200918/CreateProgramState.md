**Example 1: 进程监控信息**



Input: 

```
tccli ump CreateProgramState --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --ProgramStateItems.0.ServerIp 192.168.1.1 \
    --ProgramStateItems.0.ProgramName ops_server \
    --ProgramStateItems.0.OnlineCount 1 \
    --ProgramStateItems.0.OfflineCount 1 \
    --ProgramStateItems.0.State 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

