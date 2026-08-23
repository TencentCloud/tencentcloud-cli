**Example 1: 查询镜像关联主机资产**



Input: 

```
tccli csip DescribeImageAssociatedHostList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 807
```

Output: 
```
{
    "Response": {
        "HostList": [
            {
                "AgentStatus": "ONLINE",
                "HostName": "y*****自建集群",
                "InnerIp": "172.**.*.*",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "PublicIp": "223.160.1.1",
                "QUuid": "21fb6c0b-****-****-bd32-7739ab4d9d7c",
                "Uuid": "21fb6c0b-****-****-bd32-7739ab4d9d7c"
            }
        ],
        "TotalCount": 2,
        "RequestId": "0417863b-9e50-464c-9d4d-a026d4acae2e"
    }
}
```

