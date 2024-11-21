**Example 1: 开通服务**

开通服务，初始化资源，只针对新购资源

Input: 

```
tccli dasb DeployResource --cli-unfold-argument  \
    --VpcId vpc-1a2b3c \
    --Zone ap-guangzhou-1 \
    --ResourceId bh-saas-1a2b3c \
    --ApCode ap-guangzhou \
    --SubnetId subnet-1a2b3c \
    --CidrBlock 10.10.10.0/32 \
    --VpcName vpc1 \
    --VpcCidrBlock 10.10.0.0/16 \
    --SubnetName subnet1
```

Output: 
```
{
    "Response": {
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

