**Example 1: Checks secondary CIDR block conflicts**

CIDR block does not conflict with the existing VPC information.

Input: 

```
tccli vpc CheckAssistantCidr --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-12345678\
    --NewCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "ConflictSourceSet": [
            {
                "ConflictSourceId": "vpc-12345678",
                "SourceItem": "172.16.0.0/24",
                "ConflictItemSet": [
                    {
                        "ConflictId": "pcx-12345678",
                        "DestinationItem": "172.16.0.0/16"
                    }
                ]
            }
        ],
        "RequestId": "6e57b8db-4307-4135-b513-8c3d0e12aa4e"
    }
}
```

**Example 2: Checks secondary CIDR block conflicts-2**

CIDR block conflicts with the existing VPC information.

Input: 

```
tccli vpc CheckAssistantCidr --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-12345678\
    --NewCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "ConflictSourceSet": [],
        "RequestId": "e906fed4-292c-44ba-a240-f5bde9fd84c7"
    }
}
```

