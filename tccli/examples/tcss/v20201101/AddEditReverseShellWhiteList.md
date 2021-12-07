**Example 1: 添加反弹shell白名单**



Input: 

```
tccli tcss AddEditReverseShellWhiteList --cli-unfold-argument  \
    --WhiteListInfo.DstIp xxx \
    --WhiteListInfo.ImageIds xxxx \
    --WhiteListInfo.DstPort 12345 \
    --WhiteListInfo.ProcessName xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

**Example 2: 编辑白名单**



Input: 

```
tccli tcss AddEditReverseShellWhiteList --cli-unfold-argument  \
    --WhiteListInfo.DstIp xxxx \
    --WhiteListInfo.ImageIds xxxx \
    --WhiteListInfo.DstPort 12345 \
    --WhiteListInfo.ProcessName xxx \
    --WhiteListInfo.Id xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

