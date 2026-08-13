**Example 1: 提交漏洞修复任务**



Input: 

```
tccli csip CreateVulFixTask --cli-unfold-argument  \
    --FixItems.0.VulId 10001 \
    --FixItems.0.InstanceIds ins-a1b2c3d4 \
    --FixItems.1.KBId 20001 \
    --FixItems.1.InstanceIds ins-e5f6g7h8 ins-i9j0k1l2 \
    --Timeout 3600 \
    --CreateSnapshot False \
    --MemberId mem-tencent-6f**************
```

Output: 
```
{
    "Response": {
        "TaskId": 10001,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

