**Example 1: 添加反弹shell白名单**



Input: 

```
tccli tcss AddEditReverseShellWhiteList --cli-unfold-argument  \
    --WhiteListInfo.DstIp 127.0.0.1 \
    --WhiteListInfo.ImageIds sha256:xxxx \
    --WhiteListInfo.DstPort 12345 \
    --WhiteListInfo.ProcessName test
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

