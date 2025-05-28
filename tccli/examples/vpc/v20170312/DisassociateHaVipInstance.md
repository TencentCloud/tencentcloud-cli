**Example 1: HAVIP解绑网卡**

将网卡从HAVIP漂移范围解绑。

Input: 

```
tccli vpc DisassociateHaVipInstance --cli-unfold-argument  \
    --HaVipAssociationSet.0.HaVipId havip-crb65sya \
    --HaVipAssociationSet.0.InstanceId eni-pzrckpyd \
    --HaVipAssociationSet.0.InstanceType ENI
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 2: HAVIP解绑子机**

将子机从HAVIP漂移范围解绑。

Input: 

```
tccli vpc DisassociateHaVipInstance --cli-unfold-argument  \
    --HaVipAssociationSet.0.HaVipId havip-crb65sya \
    --HaVipAssociationSet.0.InstanceId ins-nkgrfbic \
    --HaVipAssociationSet.0.InstanceType CVM
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

