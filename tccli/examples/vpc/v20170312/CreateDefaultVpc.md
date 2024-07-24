**Example 1: 创建默认VPC**

创建默认VPC

Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "vpc-pin7sxcd",
            "SubnetId": "subnet-ixzf2m42",
            "VpcName": "abc",
            "SubnetName": "abc",
            "CidrBlock": "10.0.0.0/8"
        },
        "RequestId": "a2353d77-5c08-49c4-a28a-632a8af5e294"
    }
}
```

**Example 2: 强制生产默认VPC**

强制创建默认VPC

Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument  \
    --Force true
```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "vpc-8mpwlbdv",
            "SubnetId": "subnet-l9emqwnw",
            "VpcName": "abc",
            "SubnetName": "abc",
            "CidrBlock": "10.0.0.0/8"
        },
        "RequestId": "91348b0a-6846-49ff-822b-a21eef848c9f"
    }
}
```

**Example 3: 用户账号网络属性（DescribeAccountAttributes）同时支持基础网络和VPC，不强制创建默认VPC，则返回VpcId为0，表示不创建默认VPC**

不强制创建默认VPC

Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "0",
            "SubnetId": "subnet-jwjj37i0",
            "VpcName": "abc",
            "SubnetName": "abc",
            "CidrBlock": "10.0.0.0/8"
        },
        "RequestId": "c52dda11-9e53-440f-b034-6292f2144dd0"
    }
}
```

