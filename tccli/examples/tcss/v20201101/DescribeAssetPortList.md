**Example 1: 查询端口占用列表**

查询端口占用列表

Input: 

```
tccli tcss DescribeAssetPortList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ContainerName": "容器名称",
                "ContainerPID": 1,
                "ContainerPort": 8080,
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "tke_cls-111111",
                "ListenContainer": "tcp://:::8080",
                "ListenHost": "10.0.0.1",
                "NodeID": "mix-GOmf****",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "ProcessName": "sh",
                "PublicIP": "10.0.1.92",
                "PublicIp": "1.1.1.1",
                "PublicPort": 0,
                "RunAs": "root:root",
                "Type": "tcp"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

