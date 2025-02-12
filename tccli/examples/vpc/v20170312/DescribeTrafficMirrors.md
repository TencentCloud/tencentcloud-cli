**Example 1: 查询流量镜像实例信息**

查询流量镜像实例信息

Input: 

```
tccli vpc DescribeTrafficMirrors --cli-unfold-argument  \
    --TrafficMirrorIds  \
    --Filters.Name  \
    --Filters.Values 
```

Output: 
```
{
    "Response": {
        "TrafficMirrorSet": [
            {
                "VpcId": "vpc-dh0wcvhp",
                "TrafficMirrorId": "imgf-dh0wcvhp",
                "TrafficMirrorName": "test",
                "TrafficMirrorDescribe": "test",
                "State": "RUNNING",
                "Direction": "INGRESS",
                "CollectorSrcs": [
                    "eni-dh0wcvhp"
                ],
                "NatId": "",
                "CollectorNormalFilters": [
                    {
                        "SrcNet": "10.0.0.0/24",
                        "DstNet": "192.168.0.0/24",
                        "SrcPort": "5000",
                        "DstPort": "3456",
                        "Protocol": "TCP"
                    }
                ],
                "CollectorTarget": {
                    "TargetIps": [
                        "172.16.0.3"
                    ],
                    "AlgHash": "ENI",
                    "TargetEndPoints": [],
                    "TargetType": "ENI"
                },
                "CreateTime": "2021-08-09 15:44:30",
                "Type": 1,
                "SubnetId": "subnet-dh0wcvhp",
                "TargetInfo": [
                    {
                        "TargetId": "eni-dh0wcvhp",
                        "TargetName": "test"
                    }
                ]
            }
        ],
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

