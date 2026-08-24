**Example 1: 获取 Deployment Token**



Input: 

```
tccli ags AcquireDeploymentToken --cli-unfold-argument  \
    --DeploymentId dpl-a1b2c3d4
```

Output: 
```
{
    "Response": {
        "Token": "dpt_ZXhhbXBsZS10b2tlbg",
        "ExpiresAt": "2026-08-07T08:00:00Z",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

