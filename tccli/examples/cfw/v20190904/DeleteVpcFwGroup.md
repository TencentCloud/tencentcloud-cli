**Example 1: 删除防火墙(组)**

创建防火墙(组)

Input: 

```
tccli cfw DeleteVpcFwGroup --cli-unfold-argument  \
    --FwGroupId cfwg-0752de63 \
    --DeleteFwGroup 0 \
    --VpcFwInsList cfwew-0752de63
```

Output: 
```
{
    "Response": {
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

