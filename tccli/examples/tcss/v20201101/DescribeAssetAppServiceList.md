**Example 1: 查询app服务列表**

查询app服务列表

Input: 

```
tccli tcss DescribeAssetAppServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccessLog": "",
                "Config": "",
                "ContainerId": "3a37fab5d1d330a0bc243607d5091649c7546495fdb39f009db49ac062f3b143",
                "ContainerName": "/k8s_k8s-csp-osd-container_csp-pod-osd-1_tcs-system_6e47070d-360a-49e6-b10e-91daa81162aa_1",
                "DataPath": "",
                "ErrorLog": "",
                "Exe": "/usr/sbin/rpcbind",
                "HostID": "e1c1db55-3752-4f4e-b88a-158a87549991",
                "HostIP": "10.0.0.142",
                "HostName": "tcs-test2",
                "Listen": [
                    "tcp://:::111",
                    "tcp://0.0.0.0:111"
                ],
                "MainType": "app",
                "NodeID": "",
                "NodeType": "NORMAL",
                "NodeUniqueID": "",
                "Parameter": "/sbin/rpcbind -w",
                "Pids": [
                    66771
                ],
                "PodIP": "",
                "PodName": "",
                "ProcessCnt": 0,
                "PublicIp": "1.2.3.4",
                "RunAs": "rpc:rpc",
                "ServiceID": "fe72109ce260dbb137e60e1f20401c011256299843",
                "Type": "rpcbind",
                "Version": "",
                "WebRoot": ""
            }
        ],
        "RequestId": "66fccb1f-f7cf-4020-ba91-e60d78d77c71",
        "TotalCount": 1212
    }
}
```

