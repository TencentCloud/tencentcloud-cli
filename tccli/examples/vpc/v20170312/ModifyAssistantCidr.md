**Example 1: Only modify CIDR block**

Add secondary CIDR block: 172.16.1.0/24.

Input: 

```
tccli vpc ModifyAssistantCidr --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpcId vpc-12345678 \
    --NewCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "AssistantCidrSet": [
            {
                "VpcId": "vpc-12345678",
                "CidrBlock": "172.16.0.0/24",
                "AssistantType": 0
            }
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

**Example 2: Modifies (add and delete) auxliary CIDR block**

Add secondary CIDR block 172.16.1.0/24 while deleting 172.16.0.0/24.

Input: 

```
tccli vpc ModifyAssistantCidr --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpcId vpc-12345678 \
    --NewCidrBlocks 172.16.1.0/24 \
    --OldCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "AssistantCidrSet": [
            {
                "VpcId": "vpc-12345678",
                "CidrBlock": "172.16.1.0/24",
                "AssistantType": 0
            }
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

