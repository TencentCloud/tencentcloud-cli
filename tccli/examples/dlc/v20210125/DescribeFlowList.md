**Example 1: DescribeFlowList**



Input: 

```
tccli dlc DescribeFlowList --cli-unfold-argument  \
    --PartitionCode dlc-p-5f246106 \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "FlowInfoList": [
            {
                "FlowId": 65,
                "Status": 2,
                "WorkFlowCode": "CREATE_PARTITION"
            }
        ],
        "Total": 1,
        "RequestId": "7558a775-5f51-4d6a-940f-25011407f143"
    }
}
```

