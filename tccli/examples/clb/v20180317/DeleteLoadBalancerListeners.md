**Example 1: 删除负载均衡下的多个监听器**



Input: 

```
tccli clb DeleteLoadBalancerListeners --cli-unfold-argument  \
    --LoadBalancerId lb-db2nt5l2 \
    --ListenerIds lbl-jmgysito lbl-3bgc6o9a
```

Output: 
```
{
    "Response": {
        "RequestId": "9706db49-a5d4-413a-9610-7aa1075517e1"
    }
}
```

**Example 2: 删除一个负载均衡下的所有监听器**



Input: 

```
tccli clb DeleteLoadBalancerListeners --cli-unfold-argument  \
    --LoadBalancerId lb-db2nt5l2
```

Output: 
```
{
    "Response": {
        "RequestId": "c1157c81-f3dc-4f2a-9346-76f161d548eb"
    }
}
```

