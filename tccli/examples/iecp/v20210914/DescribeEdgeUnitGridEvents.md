**Example 1: 查询边缘单元Grid事件列表**



Input: 

```
tccli iecp DescribeEdgeUnitGridEvents --cli-unfold-argument  \
    --EdgeUnitId 100020 \
    --GridName qqq-grid \
    --Namespace default \
    --WorkloadKind DeploymentGrid \
    --NodeUnit asda-zone \
    --PodName qqq-grid-asda-zone-67fbb86b76-92cpf
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "EventSet": [
            {
                "FirstTime": "2021-08-11 21:41:52",
                "LastTime": "2021-08-17 15:06:57",
                "InvolvedObjectKind": "Pod",
                "InvolvedObjectName": "qqq-grid-asda-zone-67fbb86b76-92cpf",
                "Type": "Normal",
                "Reason": "Pulling",
                "Message": "Pulling image \"1.com/ssss:1.3\"",
                "Count": 1614,
                "NodeName": "dev-node-1"
            },
            {
                "FirstTime": "2021-08-11 21:41:53",
                "LastTime": "2021-08-17 15:02:00",
                "InvolvedObjectKind": "Pod",
                "InvolvedObjectName": "qqq-grid-asda-zone-67fbb86b76-92cpf",
                "Type": "Normal",
                "Reason": "BackOff",
                "Message": "Back-off pulling image \"1.com/ssss:1.3\"",
                "Count": 36335,
                "NodeName": "dev-node-1"
            },
            {
                "FirstTime": "2021-08-11 21:41:53",
                "LastTime": "2021-08-17 15:57:00",
                "InvolvedObjectKind": "Pod",
                "InvolvedObjectName": "qqq-grid-asda-zone-67fbb86b76-92cpf",
                "Type": "Warning",
                "Reason": "Failed",
                "Message": "Error: ImagePullBackOff",
                "Count": 36578,
                "NodeName": "dev-node-1"
            }
        ]
    }
}
```

