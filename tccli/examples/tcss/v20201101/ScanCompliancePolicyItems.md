**Example 1: 重新检测选定的检测项**



Input: 

```
tccli tcss ScanCompliancePolicyItems --cli-unfold-argument  \
    --CustomerPolicyItemIdSet 123 456 789
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TaskId": 123
    }
}
```

