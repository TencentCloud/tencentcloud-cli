**Example 1: 实例1**



Input: 

```
tccli bh DeployResource --cli-unfold-argument  \
    --ResourceId bh-saas-************ \
    --ApCode ap-guangzhou \
    --Zone ap-guangzhou-6 \
    --VpcId vpc-q1of5*** \
    --SubnetId subnet-dp102ji4 \
    --CidrBlock 192.168.24.0/24 \
    --VpcName gordan-test1 \
    --VpcCidrBlock 192.168.0.0/16 \
    --SubnetName zone6 \
    --WebAccess 1 \
    --ClientAccess 1 \
    --IntranetAccess 1 \
    --ExternalAccess 1 \
    --DeploySubnets.0.SubnetId subnet-dp102*** \
    --DeploySubnets.0.SubnetName zone6 \
    --DeploySubnets.0.Zone ap-guangzhou-6 \
    --DeploySubnets.0.SubnetCidrBlock 192.168.24.0/24 \
    --IntranetVpcId vpc-q1of5*** \
    --IntranetVpcCidrBlock 192.168.0.0/16 \
    --IntranetVpcName gordan-test1 \
    --IntranetSubnets.0.SubnetId subnet-dp102*** \
    --IntranetSubnets.0.SubnetName zone6 \
    --IntranetSubnets.0.Zone ap-guangzhou-6 \
    --IntranetSubnets.0.SubnetCidrBlock 192.168.24.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "6e4ae08b-bcca-43a2-86f3-2c3613154299"
    }
}
```

