**Example 1: 获取集群详细实例**



Input: 

```
tccli iecp DescribeEdgeUnitCloud --cli-unfold-argument  \
    --EdgeUnitId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "61abe8f0-ef42-4432-ad55-6092baaec209",
        "Name": "test-11",
        "Description": "字符串",
        "CreateTime": "2021-10-09 15:49:37",
        "UpdateTime": "2021-10-09 15:49:37",
        "LiveTime": "2021-10-09 16:15:40",
        "MasterStatus": "Running",
        "K8sVersion": "1.16.7",
        "PodCIDR": "10.1.0.0/16",
        "ServiceCIDR": "10.2.0.0/16",
        "APIServerAddress": "11.38.56.131:11302",
        "APIServerExposeAddress": "211.159.144.178:443",
        "UID": "600000559632",
        "UnitID": 5,
        "Cluster": "cls-g6uuoeez",
        "Node": {
            "NotActive": 0,
            "Offline": 0,
            "Total": 1,
            "Abnormal": 0,
            "Online": 1
        },
        "Grid": {
            "NotActive": 0,
            "Offline": 0,
            "Total": 0,
            "Abnormal": 0,
            "Online": 0
        },
        "Workload": {
            "NotActive": 1,
            "Offline": 1,
            "Total": 1,
            "Abnormal": 1,
            "Online": 1
        },
        "SubDevice": null
    }
}
```

