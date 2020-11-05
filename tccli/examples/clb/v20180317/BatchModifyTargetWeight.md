**Example 1: Modifying real server weights in batches**

This example shows you how to modify the weight of the real server `ins-19404pl5` (port 110) bound to the forwarding rule `loc-o8cnyw6c` under the listener `lbl-4b5hnc9a` in the CLB instance `lb-dx98lwo0` to 50, and modify the weight of the real server `ins-19411tzv` (port 80) bound to the forwarding rule `loc-8c5pdrb8` under the listener `lbl-20jjtaaw` to 30.

Input: 

```
tccli clb BatchModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-dx98lwo0\
    --ModifyList.0.ListenerId lbl-4b5hnc9a\
    --ModifyList.0.LocationId loc-o8cnyw6c\
    --ModifyList.0.Targets.0.InstanceId ins-19404pl5\
    --ModifyList.0.Targets.0.Port 110\
    --ModifyList.0.Targets.0.Weight 50\
    --ModifyList.1.ListenerId lbl-20jjtaaw\
    --ModifyList.1.LocationId loc-8c5pdrb8\
    --ModifyList.1.Targets.0.InstanceId ins-19411tzv\
    --ModifyList.1.Targets.0.Port 80\
    --ModifyList.1.Targets.0.Weight 30
```

Output: 
```
{
    "Response": {
        "RequestId": "83329908-a282-4f9f-8ab-031a3025b377"
    }
}
```

**Example 2: Modifying weights of servers bound to layer-4 and layer-7 listeners in batches**

This example shows you how to modify the weights of servers for layer-4 and layer-7 listeners under a CLB instance at the same time.

Input: 

```
tccli clb BatchModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-1kkno9qf\
    --ModifyList.0.ListenerId lbl-mhtffs09\
    --ModifyList.0.Targets.0.InstanceId ins-kjp6cb2f\
    --ModifyList.0.Targets.0.Port 79\
    --ModifyList.0.Targets.0.Weight 50\
    --ModifyList.1.ListenerId lbl-661zpn3b\
    --ModifyList.1.LocationId loc-78p1r0vb\
    --ModifyList.1.Targets.0.EniIp 10.202.0.96\
    --ModifyList.1.Targets.0.Port 123\
    --ModifyList.1.Targets.0.Weight 30
```

Output: 
```
{
    "Response": {
        "RequestId": "38bab2ce-616d-412c-a4b0-36110d5b17a3"
    }
}
```

