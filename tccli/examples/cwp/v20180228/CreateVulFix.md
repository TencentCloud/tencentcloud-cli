**Example 1: 提交漏洞修护**

提交漏洞修护

Input: 

```
tccli cwp CreateVulFix --cli-unfold-argument  \
    --CreateVulFixTaskQuuids.0.Quuids xx \
    --CreateVulFixTaskQuuids.0.VulId 1 \
    --SnapshotName xx \
    --SaveDays 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4",
        "FixId": 1
    }
}
```

