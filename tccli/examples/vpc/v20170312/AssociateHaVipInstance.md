**Example 1: HAVIP绑定网卡**

限制HAVIP只能在指定的网卡范围内漂移。

Input: 

```
tccli vpc AssociateHaVipInstance --cli-unfold-argument  \
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

**Example 2: HAVIP绑定子机**

限制HAVIP只能在指定的子机范围内漂移。

Input: 

```
tccli vpc AssociateHaVipInstance --cli-unfold-argument  \
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

