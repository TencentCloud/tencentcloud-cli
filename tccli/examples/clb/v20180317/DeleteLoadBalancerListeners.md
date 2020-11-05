**Example 1: Deleting all listeners of a CLB instance**



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

**Example 2: Deleting multiple listeners of a CLB instance**



Input: 

```
tccli clb DeleteLoadBalancerListeners --cli-unfold-argument  \
    --LoadBalancerId lb-db2nt5l2\
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

