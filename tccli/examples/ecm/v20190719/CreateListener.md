**Example 1: 创建负载均衡监听器**



Input: 

```
tccli ecm CreateListener --cli-unfold-argument  \
    --LoadBalancerId lb-f9zyj3kb \
    --Ports 13001 13002 13003 \
    --Protocol TCP
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-knd4jr8m",
            "lbl-2fcyclbg",
            "lbl-m5f7z60y"
        ],
        "RequestId": "28b4ba78-0100-4ebe-8afd-a09cf09a6ffe"
    }
}
```

