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
                "AccessLog": "",
                "Config": "/etc/nginx/nginx.conf",
                "ContainerId": "dbbd1295d632365",
                "ContainerName": "/container_name",
                "DataPath": "",
                "ErrorLog": "",
                "Exe": "/usr/sbin/nginx",
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "机器名称",
                "Listen": [
                    "tcp://0.0.0.0:8080"
                ],
                "MainType": "web",
                "NodeID": "",
                "NodeType": "NORMAL",
                "NodeUniqueID": "",
                "Parameter": "nginx: master process nginx -g daemon off;",
                "Pids": [
                    1,
                    2
                ],
                "PodIP": "",
                "PodName": "",
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

