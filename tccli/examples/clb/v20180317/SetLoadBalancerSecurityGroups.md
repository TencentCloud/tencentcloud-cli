**Example 1: 绑定多个安全组至负载均衡实例**

负载均衡实例原来未绑定任何安全组，执行本操作后，安全组 sg-0936o7sd、sg-12345678 将被绑定至此负载均衡实例。

Input: 

```
tccli clb SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00 \
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

**Example 2: 从负载均衡实例解绑一个安全组**

负载均衡实例原来绑定了两个安全组： sg-0936o7sd、sg-12345678，执行本操作后，安全组 sg-12345678 将从此负载均衡实例解绑。

Input: 

```
tccli clb SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00 \
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

**Example 3: 解绑所有安全组**

负载均衡实例原来已绑定若干个安全组，执行本操作后，所有安全组都将从此负载均衡实例解绑。

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

