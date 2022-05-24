**Example 1: 查询容器信息**



Input: 

```
tccli tcss DescribeAssetContainerDetail --cli-unfold-argument  \
    --ContainerId cndajlhcklanca
```

Output: 
```
{
    "Response": {
        "AppCnt": 0,
        "CPUUsage": 0,
        "Cmd": "/pause",
        "ComponentCnt": 0,
        "ContainerName": "/k8s_POD_ip-masq-agent-nhwn8_kube-system_56279ed6-af85-11e8-90de-0a587f84039e_0",
        "CreateTime": "2018-09-03T14:26:28Z",
        "HostID": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
        "HostIP": "172.16.0.4",
        "HostStatus": "",
        "ImageCreateTime": "2014-07-19T07:02:32Z",
        "ImageID": "sha256:f9d5de0795395db6c50cb1ac82ebed1bd8eb3eefcebb1aa724e01239594e937b",
        "ImageName": "ccr.ccs.tencentyun.com/library/pause:latest",
        "ImageSize": 239840,
        "K8sMaster": "",
        "Mounts": [],
        "Network": {
            "EndpointID": "912b40bfbddd044734e42135bc0a6a49984048ccdf26687d824f2d52cb63c650",
            "Gateway": "",
            "Ipv4": "",
            "Ipv6": "",
            "MAC": "",
            "Mode": "host",
            "Name": "",
            "NetworkID": "327b241f90565248657f72ead20c1adfbac8dd60b18f7abf0a9727f2ff7ffc49"
        },
        "POD": "",
        "PortCnt": 0,
        "ProcessCnt": 0,
        "RamUsage": 0,
        "RequestId": "9915f397-3268-4c12-85c9-03b07b6db718",
        "RunAs": "",
        "Status": "exited",
        "WebServiceCnt": 0,
        "NetStatus": "",
        "NetSubStatus": "",
        "IsolateSource": "xx",
        "IsolateTime": "xx"
    }
}
```

