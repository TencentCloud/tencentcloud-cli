**Example 1: 上报服务回调地址注册**



Input: 

```
tccli ump ReportServiceRegister --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --ServerIp 192.168.1.1 \
    --ServerNodeId asdr5qwfq451234fsdgsfg \
    --ServiceRegisterInfos.0.CgiUrl http://127.0.0.1:111111/hello_world \
    --ServiceRegisterInfos.0.ServiceType 2 \
    --ServiceRegisterInfos.1.CgiUrl http://127.0.0.1:22222/hello_tencent \
    --ServiceRegisterInfos.1.ServiceType 3 \
    --ReportTime 123456789
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

