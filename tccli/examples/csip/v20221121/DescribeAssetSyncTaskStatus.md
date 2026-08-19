**Example 1: DescribeAssetSyncTaskStatus**



Input: 

```
tccli csip DescribeAssetSyncTaskStatus --cli-unfold-argument  \
    --TaskIDs csip-2g7sp2mj \
    --MemberId mem-0ac**0f*f***d***
```

Output: 
```
{
    "Response": {
        "TaskStatus": "completed",
        "RequestId": "60ebd367-c11f-4b32-bc13-7e9ceda16945"
    }
}
```

