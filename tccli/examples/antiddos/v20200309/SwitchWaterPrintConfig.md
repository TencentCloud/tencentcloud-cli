**Example 1: 开启或关闭DDoS防护的水印防护配置**



Input: 

```
tccli antiddos SwitchWaterPrintConfig --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --OpenStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "512b8c34-3df9-448a-ae90-c28643d351bf"
    }
}
```

