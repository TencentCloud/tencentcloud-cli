**Example 1: 示例**



Input: 

```
tccli cwp DescribeServerRelatedDirInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "HostIp": "10.0.0.1",
        "HostName": "服务器1",
        "ProtectDirNum": 1,
        "ProtectFileNum": 1,
        "ProtectTamperNum": 1,
        "ProtectLinkNum": 1,
        "RequestId": "ee02ffee-8682-4b28-aae3-561274d68bdd"
    }
}
```

