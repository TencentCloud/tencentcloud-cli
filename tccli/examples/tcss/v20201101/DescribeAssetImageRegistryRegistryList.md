**Example 1: 镜像仓库查询镜像仓库列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryRegistryList --cli-unfold-argument  \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "e59f97b7-87d4-4909-8289-61bd28423d2f",
        "TotalCount": 15525,
        "List": [
            {
                "ConnDetectDetail": [
                    {
                        "ConnDetectMessage": "AgentOffline",
                        "ConnDetectStatus": "status_auth_failed",
                        "FailReason": "仓库账号密码异常",
                        "Quuid": "5a540076-d38a-4078-aa98-e7c86371d322",
                        "Solution": "请检查您的仓库账号/密码是否正确，建议重新输入，稍后重试连接",
                        "Uuid": "5a540076-d38a-4078-aa98-e7c86371d322"
                    }
                ],
                "ConnDetectHostCount": 1,
                "ConnDetectType": "agent",
                "ConnectMsg": "connect msg",
                "InstanceID": "instance-01",
                "LatestSyncTime": "2024-10-23 03:12:50",
                "Name": "aws_public",
                "NetType": "public",
                "RegistryId": 10000,
                "RegistryRegion": "default",
                "RegistryType": "aws",
                "RegistryVersion": "V1",
                "SyncFailReason": "自有主机agent离线",
                "SyncMessage": "自有主机agent离线",
                "SyncSolution": "您选择的所有自有主机agent离线，请重新检查主机节点后再进行重试",
                "SyncStatus": "failed",
                "Url": "https://public.aws"
            }
        ]
    }
}
```

