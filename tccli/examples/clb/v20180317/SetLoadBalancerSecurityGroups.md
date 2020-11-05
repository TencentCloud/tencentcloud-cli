**Example 1: Unbinding a security group from a CLB instance**

A CLB instance was previously bound to two security groups: `sg-0936o7sd` and `sg-12345678`. This example shows you how to unbind the security group `sg-12345678` from this instance.

Input: 

```
tccli clb SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00\
    --SecurityGroups sg-0936o7sd
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04644"
    }
}
```

**Example 2: Binding multiple security groups to a CLB instance**

A CLB instance was not previously bound to any security group. This example shows you how to bind the security groups `sg-0936o7sd` and `sg-12345678` to this instance.

Input: 

```
tccli clb SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00\
    --SecurityGroups sg-0936o7sd sg-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04633"
    }
}
```

**Example 3: Unbinding all security groups**

A CLB instance was previously bound to several security groups. This example shows you how to unbind all security groups from this instance.

Input: 

```
tccli clb SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04655"
    }
}
```

