**Example 1: 切换业务网络**

pxe装机结束前，切换chc物理服务器到业务网络

Input: 

```
tccli cvm ModifyChcNetworkMode --cli-unfold-argument  \
    --ChcIds chc-fc5plksv \
    --NetworkMode BUSINESS
```

Output: 
```
{
    "Response": {
        "RequestId": "41f75bb5-0a62-4a58-be1a-4181eb1514f4"
    }
}
```

**Example 2: 切换部署网络**

pxe装机开始前，切换chc物理机服务器到部署网络

Input: 

```
tccli cvm ModifyChcNetworkMode --cli-unfold-argument  \
    --ChcIds chc-nzufwq77 \
    --NetworkMode DEPLOY
```

Output: 
```
{
    "Response": {
        "RequestId": "78c8e8c2-c3b7-4ee4-9fbf-8819e688c405"
    }
}
```

