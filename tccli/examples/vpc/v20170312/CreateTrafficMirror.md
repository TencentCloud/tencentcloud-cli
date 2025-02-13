**Example 1: 创建流量镜像**

创建流量镜像

Input: 

```
tccli vpc CreateTrafficMirror --cli-unfold-argument  \
    --Direction EGRESS \
    --NatId nat-qo7kugz0 \
    --TrafficMirrorName demo \
    --State RUNNING \
    --VpcId vpc-39lpx32d \
    --CollectorTarget.AlgHash FIVE_TUPLE_FLOW \
    --CollectorTarget.TargetIps 172.16.16.10 \
    --CollectorSrcs eni-39lpv32n
```

Output: 
```
{
    "Response": {
        "TrafficMirror": {
            "VpcId": "vpc-fo8nfm00",
            "TrafficMirrorId": "imgf-ewrpvb00",
            "TrafficMirrorName": "UpdateTrafficMirrorDirection_tUhhZ7Jj",
            "TrafficMirrorDescribe": "",
            "State": "RUNNING",
            "Direction": "EGRESS",
            "CollectorSrcs": [
                "eni-4qq71jmz"
            ],
            "NatId": "",
            "CollectorNormalFilters": [],
            "CollectorTarget": {
                "AlgHash": "ENI",
                "TargetType": "IP",
                "TargetIps": [
                    "10.0.0.0"
                ],
                "TargetEndPoints": []
            },
            "CreateTime": "0000-00-00 00:00:00"
        },
        "RequestId": "941e5605-e17c-45b8-bd80-031386e29559"
    }
}
```

