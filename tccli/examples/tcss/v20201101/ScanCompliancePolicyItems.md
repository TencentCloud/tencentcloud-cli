**Example 1: 重新检测选定的检测项**



Input: 

```
tccli tcss ScanCompliancePolicyItems --cli-unfold-argument  \
    --CustomerPolicyItemIdSet 111 456 789
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "TaskId": 1001
    }
}
```

