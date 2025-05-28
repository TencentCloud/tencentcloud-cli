**Example 1: 创建安卓实例 WebShell 连接**



Input: 

```
tccli gs CreateAndroidInstanceWebShell --cli-unfold-argument  \
    --AndroidInstanceId cai-123456-abc
```

Output: 
```
{
    "Response": {
        "Key": "key-01",
        "Address": "ap-shenzhen-1.webssh.crtrcloud.com",
        "Zone": "ap-shenzhen-1",
        "ConnectUrl": "https://ex-cloud-gaming.crtrcloud.com/cloud_gaming_web/webterm/index.html?container=xxx&shell-key=xxxx&shell-addr=ap-shenzhen-1.webssh.crtrcloud.com",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

