**Example 1: DescribeFlowDetailList**



Input: 

```
tccli dlc DescribeFlowDetailList --cli-unfold-argument  \
    --PartitionCode dlc-p-5f246106 \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "FlowDetailList": [
            {
                "Activities": [
                    {
                        "ActivityCode": "ACQUIRE_RESOURCE_POOL",
                        "CreateTime": "2026-03-14T23:08:34",
                        "Duration": 1,
                        "Status": 2
                    }
                ],
                "CreateTime": "2026-03-14T23:08:34",
                "FlowId": 65,
                "Progress": 100,
                "Status": 2,
                "WorkFlowCode": "CREATE_PARTITION",
                "WorkFlowId": "wf-b262cf27-dlc-p-5f246106"
            }
        ],
        "Total": 1,
        "RequestId": "e2883ff2-2fbc-431d-beb5-80873a677020"
    }
}
```

