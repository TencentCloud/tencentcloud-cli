**Example 1: 提交漏洞修护**

提交漏洞修护

Input: 

```
tccli cwp CreateVulFix --cli-unfold-argument  \
    --CreateVulFixTaskQuuids.0.Quuids 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --CreateVulFixTaskQuuids.0.VulId 1 \
    --SnapshotName 快照名称 \
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

