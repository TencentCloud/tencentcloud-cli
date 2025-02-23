**Example 1: 创建示例**

创建一个私有连接，用于用户VPC访问TIONE

Input: 

```
tccli tione CreatePrivateLink --cli-unfold-argument  \
    --ServiceGroupId ms-22c9njmt \
    --VpcId vpc-314xh0ko \
    --SubnetId subnet-8ra6pdq7
```

Output: 
```
{
    "Response": {
        "RequestId": "b8f848e4-64ea-475c-864e-6d4b0c9ec6ea"
    }
}
```

