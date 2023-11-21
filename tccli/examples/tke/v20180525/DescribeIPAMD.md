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
        "DisableVpcCniMode": false,
        "EnableCustomizedPodCidr": false,
        "EnableIPAMD": false,
        "Phase": "running",
        "Reason": "",
        "RequestId": "c692a3b6-11cd-4a9d-8e36-409545d332a2",
        "SubnetIds": [
            "subnet-imgoatdg"
        ],
        "ClaimExpiredDuration": "300s"
    }
}
```

