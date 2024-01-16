**Example 1: 开通服务**

开通服务，初始化资源，只针对新购资源

Input: 

```
tccli dasb DeployResource --cli-unfold-argument  \
    --VpcId vpc-xxxxxx \
    --Zone ap-guangzhou-1 \
    --ResourceId bh-saas-xxxxxx \
    --ApCode ap-guangzhou \
    --SubnetId subnet-xxxxxx \
    --CidrBlock 10.10.10.0/32 \
    --VpcName vpc1 \
    --VpcCidrBlock 10.10.0.0/16 \
    --SubnetName subnet1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

