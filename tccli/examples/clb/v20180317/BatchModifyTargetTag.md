**Example 1: 设置标签**



Input: 

```
tccli clb BatchModifyTargetTag --cli-unfold-argument  \
    --LoadBalancerId lb-xxxxxxxx \
    --ModifyList.0.ListenerId lbl-yyyyyyyy \
    --ModifyList.0.Targets.0.Port 1000 \
    --ModifyList.0.Targets.0.EniIp 1.1.1.1 \
    --ModifyList.0.Targets.0.Tag tag-target
```

Output: 
```
{
    "Response": {
        "RequestId": "9cc30f1d-c237-422a-87ff-8f08c31a46e6"
    }
}
```

