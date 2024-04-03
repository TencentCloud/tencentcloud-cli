**Example 1: 查询未开通加速的VPC**



Input: 

```
tccli vpc DescribeOverseaAccelerator --cli-unfold-argument  \
    --VpcId vpc-40omdvr7
```

Output: 
```
{
    "Response": {
        "AccelerateDomain": [],
        "RequestId": "c1993729-f26e-4322-8320-462979693961"
    }
}
```

**Example 2: 查询一个VPC的已加速域名**

查询一个VPC的已加速域名

Input: 

```
tccli vpc DescribeOverseaAccelerator --cli-unfold-argument  \
    --VpcId vpc-8enostyw
```

Output: 
```
{
    "Response": {
        "AccelerateDomain": [
            {
                "Domain": "buy.itunes.apple.com",
                "DomainShort": "APPLEPAY"
            }
        ],
        "RequestId": "e4de1feb-adaf-4cfd-ad3c-db9aecfe549d"
    }
}
```

