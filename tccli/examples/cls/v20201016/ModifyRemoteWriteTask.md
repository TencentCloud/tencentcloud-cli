**Example 1: 修改RemoteWrite 任务详情**

修改RemoteWrite 任务详情

Input: 

```
tccli cls ModifyRemoteWriteTask --cli-unfold-argument  \
    --TaskId d0f385dc-218b-4bda-bc7f-27d27c22fdd6 \
    --TopicId 680640a3-96d9-476f-afbd-f4492773a21f \
    --Enable 1 \
    --NetType 3 \
    --VpcId vpc-0******l \
    --RemoteWriteURL http://****.**6:90**/api/v1/prom/write \
    --VirtualGatewayType 1025
```

Output: 
```
{
    "Response": {
        "RequestId": "7034f990-1f3b-484c-87dd-43b423d3aa70"
    }
}
```

