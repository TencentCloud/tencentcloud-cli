**Example 1: 修改子网DHCP Relay属性**

修改子网DHCP Relay属性

Input: 

```
tccli bmvpc ModifySubnetDHCPRelay --cli-unfold-argument  \
    --VpcId vpc-q1j48dkd \
    --SubnetId subnet-q1j48dkd \
    --EnableDHCP false
```

Output: 
```
{
    "Response": {
        "RequestId": "30a4b438-a5f1-4fca-a34e-95dfd07695ca"
    }
}
```

