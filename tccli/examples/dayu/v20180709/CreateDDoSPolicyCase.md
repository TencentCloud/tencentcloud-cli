**Example 1: 添加策略场景**



Input: 

```
tccli dayu CreateDDoSPolicyCase --cli-unfold-argument  \
    --Business bgpip \
    --CaseName testpolicycase \
    --PlatformTypes PC TV \
    --AppType WEB \
    --AppProtocols tcp \
    --TcpPortList 80,443,600-700,888 \
    --UdpPortList 80,443,600-700,888
```

Output: 
```
{
    "Response": {
        "SceneId": "scene-000003h7",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

