**Example 1: 查询app服务列表**



Input: 

```
tccli tcss DescribeAssetAppServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ServiceID": "366135633765366230363863343763336265316533306562623030643364393731323536323939383433",
                "HostID": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "HostIP": "172.16.0.4",
                "ContainerName": "/k8s_sidecar_kube-dns-7f687bdf4-s29r7_kube-system_c4cdbd2c-af84-11e8-90de-0a587f84039e_1",
                "MainType": "app",
                "Type": "sidecar",
                "Version": "",
                "RunAs": "nobody:nobody",
                "Exe": "/sidecar",
                "Config": "",
                "ProcessCnt": 0,
                "AccessLog": "",
                "ErrorLog": "",
                "DataPath": "",
                "WebRoot": "",
                "Pids": [
                    2693
                ],
                "Listen": [
                    "tcp://:::10054"
                ],
                "Parameter": "/sidecar --v=2 --logtostderr --probe=kubedns,127.0.0.1:10053,kubernetes.default.svc.cluster.local,5,A --probe=dnsmasq,127.0.0.1:53,kubernetes.default.svc.cluster.local,5,A",
                "ContainerId": "a4b2d7595c09ebc2d1c815ab040270154ee11da28afb3629d57ee7a7b3a5bf69"
            }
        ],
        "RequestId": "5e1e8870-766a-4a72-bbc6-d9bad2088526",
        "TotalCount": 14
    }
}
```

