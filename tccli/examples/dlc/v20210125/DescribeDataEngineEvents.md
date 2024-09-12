**Example 1: test**



Input: 

```
tccli dlc DescribeDataEngineEvents --cli-unfold-argument  \
    --Limit 0 \
    --DataEngineName DataEngine-ftvxxx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "ClusterInfo": [
                    "缩容前：集群个数1个，集群规模16CU，缩容后:集群个数0个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群缩容完成"
                ],
                "Time": [
                    "2024-07-22 19:58:28"
                ]
            },
            {
                "ClusterInfo": [
                    "引擎已挂起，原因：自动挂起"
                ],
                "EventsAction": [
                    "引擎挂起"
                ],
                "Time": [
                    "2024-07-22 19:58:08"
                ]
            },
            {
                "ClusterInfo": [
                    "扩容前：集群个数0个，集群规模16CU，扩容后:集群个数1个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群扩容完成"
                ],
                "Time": [
                    "2024-07-22 19:55:09"
                ]
            },
            {
                "ClusterInfo": [
                    "扩容前：集群个数0个，集群规模16CU，扩容后:集群个数1个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群开始扩容"
                ],
                "Time": [
                    "2024-07-22 19:52:39"
                ]
            },
            {
                "ClusterInfo": [
                    "引擎已恢复，原因：自动恢复"
                ],
                "EventsAction": [
                    "集群恢复"
                ],
                "Time": [
                    "2024-07-22 19:52:06"
                ]
            },
            {
                "ClusterInfo": [
                    "缩容前：集群个数1个，集群规模16CU，缩容后:集群个数0个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群缩容完成"
                ],
                "Time": [
                    "2024-07-14 21:58:13"
                ]
            },
            {
                "ClusterInfo": [
                    "引擎已挂起，原因：自动挂起"
                ],
                "EventsAction": [
                    "引擎挂起"
                ],
                "Time": [
                    "2024-07-14 21:57:55"
                ]
            },
            {
                "ClusterInfo": [
                    "扩容前：集群个数0个，集群规模16CU，扩容后:集群个数1个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群扩容完成"
                ],
                "Time": [
                    "2024-07-14 21:52:25"
                ]
            },
            {
                "ClusterInfo": [
                    "扩容前：集群个数0个，集群规模16CU，扩容后:集群个数1个，集群规模16CU"
                ],
                "EventsAction": [
                    "集群开始扩容"
                ],
                "Time": [
                    "2024-07-14 21:49:56"
                ]
            },
            {
                "ClusterInfo": [
                    "引擎已恢复，原因：自动恢复"
                ],
                "EventsAction": [
                    "集群恢复"
                ],
                "Time": [
                    "2024-07-14 21:49:23"
                ]
            }
        ],
        "Page": 1,
        "RequestId": "67ce07dc-8a40-4c1f-aee6-35c7b0f7b04f",
        "Size": 10,
        "TotalCount": 198,
        "TotalPages": 20
    }
}
```

