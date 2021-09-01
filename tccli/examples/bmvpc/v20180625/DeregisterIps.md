**Example 1: 注销私有网络IP**

注销私有网络IP

Input: 

```
tccli bmvpc DeregisterIps --cli-unfold-argument  \
    --VpcId vpc-q1j48dkd \
    --IpSet 10.0.0.10
```

Output: 
```
{
    "Response": {
        "RequestId": "30a4b438-a5f1-4fca-a34e-95dfd07695ca"
    }
}
```

