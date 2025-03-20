**Example 1: 查询容器信息**

查询容器信息

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
        "ClusterID": "cls-m2x0ndjy",
        "ClusterName": "tke2",
        "Cmd": "/usr/bin/dumb-init -- /nginx-ingress-controller --publish-service=ingress-nginx/ingress-nginx-controller --election-id=ingress-controller-leader --leader-elect-retry-period=2s --leader-elect-renew-deadline=10s --leader-elect-lease-duration=15s --v=2 --ingress-class=nginx --controller-class=k8s.io/ingress-nginx --configmap=ingress-nginx/ingress-nginx-controller --watch-ingress-without-class=true --update-status-on-shutdown=false --time-buckets=0.01,0.1,1,10 --length-buckets=10,30,50,70,90 --size-buckets=10,100,1000,100000,1000****",
        "ComponentCnt": 0,
        "ContainerName": "cbs-csi",
        "CreateTime": "2024-10-24 19:36:24",
        "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "HostIP": "1.1.1.1",
        "HostStatus": "ONLINE",
        "ImageCreateTime": "0001-01-01 08:05:43",
        "ImageID": "sha256:563af",
        "ImageName": "image:latest",
        "ImageSize": 0,
        "IsolateSource": "none ",
        "IsolateTime": "1970-01-01 00:00:01",
        "K8sMaster": "etcd",
        "Mounts": [],
        "NetStatus": "NORMAL",
        "NetSubStatus": "NONE",
        "Network": {
            "EndpointID": "myService/us-west-1/instance",
            "Gateway": "gateway",
            "Ipv4": "127.0.0.1",
            "Ipv6": "2001:db8:85a3::8a2e:370:7334",
            "MAC": "00:1A:2B:3C:4D:5E",
            "Mode": "mode",
            "Name": "name",
            "NetworkID": "1002"
        },
        "NodeID": "eklet-subnet-1ewk3avk",
        "NodeName": "VM-1-254-tencentos",
        "NodeSubNetCIDR": "10.0.200.0/24",
        "NodeSubNetID": "subnet-5gu2***",
        "NodeSubNetName": "subnet***",
        "NodeType": "NORMAL",
        "NodeUniqueID": "27501aaed5e639693783321219989889",
        "POD": "tcss-aset-11-321",
        "PodIP": "1.1.1.1",
        "PodName": "tcss-asset-124321",
        "PodStatus": "Running",
        "PortCnt": 0,
        "ProcessCnt": 0,
        "PublicIP": "10.0.1.92",
        "RamUsage": 0,
        "RequestId": "6954374b-bfcd-4751-8358-3e3682551514",
        "RunAs": "root",
        "Status": "RUNNING",
        "WebServiceCnt": 0
    }
}
```

