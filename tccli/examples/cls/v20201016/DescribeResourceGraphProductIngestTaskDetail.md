**Example 1: 查询具体接入任务详情**



Input: 

```
tccli cls DescribeResourceGraphProductIngestTaskDetail --cli-unfold-argument  \
    --ResourceGraphId 562b6948-5c9e-417f-9813-f359178fc5c6 \
    --TaskId e59f3af6-0cc7-47c2-9ff9-b38cc7298895
```

Output: 
```
{
    "Response": {
        "ProductIngestTaskDetail": {
            "EBPFCollectRule": {
                "Filters": {
                    "DNS": {
                        "Mode": 0
                    },
                    "DestEndpoint": {
                        "Mode": 0
                    },
                    "ProcessName": {
                        "Mode": 1,
                        "ProcessNames": [
                            "nginx"
                        ]
                    }
                },
                "RuleName": "default-ebpf-rule",
                "TrackTarget": 1
            },
            "InstanceIds": [
                "cls-52rnx6ns"
            ],
            "ProductIngestTaskItem": {
                "CreateTime": 1782916304,
                "Name": "产品接入任务-test-tke-8",
                "Product": "tke",
                "Status": 1,
                "TaskId": "e59f3af6-0cc7-47c2-9ff9-b38cc7298895",
                "UpdateTime": 1783912748
            },
            "SelectionMode": 2,
            "TaskId": "e59f3af6-0cc7-47c2-9ff9-b38cc7298895"
        },
        "RequestId": "812d7fb6-b8b5-4626-ba22-e56a6ef50edb"
    }
}
```

