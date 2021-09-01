**Example 1: 修改策略场景**



Input: 

```
tccli dayu ModifyDDoSPolicyCase --cli-unfold-argument  \
    --Business bgpip \
    --SceneId scene-00000003 \
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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

