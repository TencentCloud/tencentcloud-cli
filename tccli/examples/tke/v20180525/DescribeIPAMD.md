**Example 1: 获取eniipamd组件信息**



Input: 

```
tccli tke DescribeIPAMD --cli-unfold-argument  \
    --ClusterId xx
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
        "RequestId": "xxxxx",
        "SubnetIds": null
    }
}
```

