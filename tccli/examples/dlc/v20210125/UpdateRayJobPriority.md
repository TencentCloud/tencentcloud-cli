**Example 1: 更新作业优先级**



Input: 

```
tccli dlc UpdateRayJobPriority --cli-unfold-argument  \
    --Id rayjob-20260323163852-huvy \
    --Priority 5
```

Output: 
```
{
    "Response": {
        "Id": "rayjob-20260323163852-huvy",
        "Status": "PENDING",
        "Priority": 5,
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

