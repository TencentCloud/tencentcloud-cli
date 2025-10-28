**Example 1: 获取eniipamd组件信息**



Input: 

```
tccli tke DescribeIPAMD --cli-unfold-argument  \
    --ClusterId cls-8k33qz0w
```

Output: 
```
{
    "Response": {
        "ClaimExpiredDuration": "0s",
        "DisableVpcCniMode": false,
        "EnableCustomizedPodCidr": true,
        "EnableIPAMD": true,
        "EnableTrunkingENI": false,
        "Phase": "running",
        "Reason": "",
        "RequestId": "93f7457a-4c95-4e23-b75f-e3bdbf1ab81e",
        "SubnetIds": [
            "subnet-7fxdi13h",
            "subnet-502b2uw9"
        ]
    }
}
```

