**Example 1: Creating a default VPC**



Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument  \
    --Version 2017-03-12
```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "vpc-pin7sxcd",
            "SubnetId": "subnet-ixzf2m42"
        },
        "RequestId": "a2353d77-5c08-49c4-a28a-632a8af5e294"
    }
}
```

**Example 2: The network attributes (DescribeAccountAttributes) of the user account support both the basic network and VPC. If a default VPC is not created as required, the returned VpcId is 0, indicating that a default VPC is not created.**



Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument  \
    --Version 2017-03-12
```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "0",
            "SubnetId": "0"
        },
        "RequestId": "c52dda11-9e53-440f-b034-6292f2144dd0"
    }
}
```

**Example 3: Creating a default VPC as required**



Input: 

```
tccli vpc CreateDefaultVpc --cli-unfold-argument  \
    --Version 2017-03-12\
    --Force true
```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "vpc-8mpwlbdv",
            "SubnetId": "subnet-l9emqwnw"
        },
        "RequestId": "91348b0a-6846-49ff-822b-a21eef848c9f"
    }
}
```

