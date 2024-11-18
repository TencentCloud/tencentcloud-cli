**Example 1: 开通服务**

开通服务，初始化资源，只针对新购资源

Input: 

```
tccli bh DeployResource --cli-unfold-argument  \
    --VpcId vpc-bhtest \
    --Zone ap-guangzhou-1 \
    --ResourceId bh-saas-bhtest \
    --ApCode ap-guangzhou \
    --SubnetId subnet-bhtest \
    --CidrBlock 10.10.10.0/32 \
    --VpcName vpc1 \
    --VpcCidrBlock 10.10.0.0/16 \
    --SubnetName subnet1
```

Output: 
```
{
    "Response": {
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7"
    }
}
```

