**Example 1: 迁移私有网络和子网**

迁移私有网络和子网

Input: 

```
tccli cvd ModifyInstancesVpc --cli-unfold-argument  \
    --SubnetId subnet-test1 \
    --VpcId vpc-test1 \
    --InstanceIds cdi-bx7b2lfkv1zplsf
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

