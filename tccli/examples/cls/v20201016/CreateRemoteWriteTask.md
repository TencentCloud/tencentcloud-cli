**Example 1: 创建RemoteWrite 任务**



Input: 

```
tccli cls CreateRemoteWriteTask --cli-unfold-argument  \
    --TopicId 80b2f456-f118-4243-ae7e-fdc1df2d1b31 \
    --Name remotewritetest \
    --Target TencentCloud_Prometheus \
    --RemoteWriteURL http://1*******6:90**/api/v1/prom/write \
    --AuthType 1 \
    --NetType 1 \
    --VpcId vpc-**** \
    --AuthInfo.Username 1********* \
    --AuthInfo.Password z****X*~W*72*=***********Ga \
    --AuthInfo.Token  \
    --VirtualGatewayType 1025 \
    --InstanceId prom-****6pmm \
    --HasServicesLog 2
```

Output: 
```
{
    "Response": {
        "TaskId": "26b30377-ed59-4f46-bafd-74734da08e83",
        "RequestId": "cfa7bf34-9f9a-4210-b6d2-0f5c20763f5d"
    }
}
```

