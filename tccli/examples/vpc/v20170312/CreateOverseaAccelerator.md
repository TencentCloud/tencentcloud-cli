**Example 1: 为VPC开通苹果支付加速**

通过短名开通苹果支付域名的访问加速

Input: 

```
tccli vpc CreateOverseaAccelerator --cli-unfold-argument  \
    --VpcId vpc-p3noywst \
    --AccelerateDomain.0.DomainShort APPLEPAY
```

Output: 
```
{
    "Response": {
        "RequestId": "0ca4797a-168a-43bf-ac4a-0cd8e20e6cdc"
    }
}
```

**Example 2: 通过完整域名为VPC开通苹果加速**



Input: 

```
tccli vpc CreateOverseaAccelerator --cli-unfold-argument  \
    --AccelerateDomain.0.Domain buy.itunes.apple.com \
    --VpcId vpc-40omdvr7
```

Output: 
```
{
    "Response": {
        "RequestId": "3c20a53a-4c85-49f9-9c68-05b52c2823da"
    }
}
```

