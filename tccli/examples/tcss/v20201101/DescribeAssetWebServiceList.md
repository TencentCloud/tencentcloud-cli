**Example 1: 查询web服务列表**

查询web服务列表

Input: 

```
tccli tcss DescribeAssetWebServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccessLog": "AccessLog",
                "Config": "/etc/nginx/nginx.conf",
                "ContainerId": "dbbd1295d632365",
                "ContainerName": "/container_name",
                "DataPath": "/a/b",
                "ErrorLog": "ErrorLog",
                "Exe": "/usr/sbin/nginx",
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "机器名称",
                "Listen": [
                    "tcp://0.0.0.0:8080"
                ],
                "MainType": "web",
                "NodeID": "mix-GOmf****",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "Parameter": "nginx: master process nginx -g daemon off;",
                "Pids": [
                    1,
                    2
                ],
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "ProcessCnt": 0,
                "PublicIp": "1.1.1.1",
                "RunAs": ":",
                "ServiceID": "27501aaed5e639693783321219989889",
                "Type": "Nginx",
                "Version": "1.22.0",
                "WebRoot": "/usr/share/nginx/html"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

