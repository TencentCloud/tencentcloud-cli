**Example 1: 查询文件配置项发布信息**



Input: 

```
tccli tsf DescribeFileConfigReleases --cli-unfold-argument  \
    --ConfigId dcfg-f-v3qqrkdy \
    --ConfigName conf_app \
    --GroupId group-vj3n6lzy \
    --NamespaceId namespace-ygo3djma \
    --ClusterId cls-f6bk82xc \
    --ApplicationId application-vw8ljmwv \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5620eba9-1673-4b3c-b375-591910b0fbc0",
        "Result": {
            "Content": [
                {
                    "ClusterId": "cls-f6bk82xc",
                    "ClusterName": "cluster-container-jolyonzheng",
                    "ConfigId": "dcfg-f-v3qqrkdy",
                    "ConfigName": "conf_app",
                    "ConfigReleaseId": "dcfgr-f-vkjjw7ny",
                    "ConfigVersion": "2",
                    "GroupId": "group-vj3n6lzy",
                    "GroupName": "group-provider",
                    "NamespaceId": "namespace-ygo3djma",
                    "NamespaceName": "cluster-container-jolyonzheng_default",
                    "ReleaseDesc": "This is desc",
                    "ReleaseTime": "2024-11-28 20:49:57"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

