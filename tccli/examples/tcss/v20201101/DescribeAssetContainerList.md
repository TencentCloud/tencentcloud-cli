**Example 1: 搜索查询容器列表**



Input: 

```
tccli tcss DescribeAssetContainerList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ContainerID": "dc26549577ae70f50f0d87d78f5ed72ce2be0607c8e83758eb200f03d23d56e4",
                "ContainerName": "/k8s_sidecar_kube-dns-7f687bdf4-llln6_kube-system_c4ab281e-af84-11e8-90de-0a587f84039e_0",
                "Status": "exited",
                "CreateTime": "2018-09-03T14:27:08Z",
                "UpdateTime": "2021-01-29T07:48:28.486Z",
                "RunAs": "",
                "Cmd": "/sidecar --v=2 --logtostderr --probe=kubedns,127.0.0.1:10053,kubernetes.default.svc.cluster.local,5,A --probe=dnsmasq,127.0.0.1:53,kubernetes.default.svc.cluster.local,5,A",
                "CPUUsage": 0,
                "RamUsage": 0,
                "ImageName": "ccr.ccs.tencentyun.com/library/k8s-dns-sidecar-amd64@sha256:97074c951046e37d3cbb98b82ae85ed15704a290cce66a8314e7f846404edde9",
                "ImageID": "sha256:38bac66034a6217abfd44b4a8a763b1a4c973045cae2763f2cc857baa5c9a872",
                "POD": "",
                "HostID": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "HostIP": "172.16.0.4"
            }
        ],
        "RequestId": "05c83fc4-d189-4d61-9947-3b845262d500",
        "TotalCount": 224
    }
}
```

