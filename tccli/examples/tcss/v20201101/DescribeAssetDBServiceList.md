**Example 1: 查询db服务列表**

查询db服务列表

Input: 

```
tccli tcss DescribeAssetDBServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccessLog": "accesslog",
                "Config": "config",
                "ContainerId": "3c0a1bc138f982b187549237eb3fc02f99616bb93be3d1b65a5f14f0649591be",
                "ContainerName": "/k8s_redis_redis-tce-redis-support-ss-0_sso_ad389998-b0ab-4d43-8b25-2c96cac55ecf_0",
                "DataPath": "/a/b",
                "ErrorLog": "errorlog",
                "Exe": "/usr/local/bin/redis-server",
                "HostID": "a9365a64-7ffa-4e6e-ab27-1a0475e65070",
                "HostIP": "10.0.0.98",
                "HostName": "tcs-pre3",
                "Listen": [
                    "tcp://0.0.0.0:6379"
                ],
                "MainType": "db",
                "NodeID": "mix-GOmf****",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "Parameter": "redis-server 0.0.0.0:6379         ",
                "Pids": [
                    338552
                ],
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "ProcessCnt": 0,
                "PublicIp": "43.138.193.64",
                "RunAs": "root:root",
                "ServiceID": "fd1a1b7d9c4bc8168949b4e3ee5e9cd91256299843",
                "Type": "redis",
                "Version": "1.0.1",
                "WebRoot": "web"
            }
        ],
        "RequestId": "57ab9e09-70b3-40ab-b42b-cd2d422dcb9d",
        "TotalCount": 89
    }
}
```

