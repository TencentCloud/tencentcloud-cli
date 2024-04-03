**Example 1: 检查辅助CIDR冲突**

CIDR与VPC现存信息存在冲突。

Input: 

```
tccli vpc CheckAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-12345678 \
    --NewCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "ConflictSourceSet": [
            {
                "ConflictSourceId": "vpcd-122d5678",
                "SourceItem": "172.16.0.0/16",
                "ConflictItemSet": [
                    {
                        "ConfilctId": "vpc-12345678",
                        "DestinationItem": "172.16.0.0/24"
                    }
                ]
            }
        ],
        "RequestId": "e906fed4-29ew-44ba-a240-f5bde9fd84c7"
    }
}
```

**Example 2: 检查辅助CIDR冲突-2**

CIDR与VPC现存信息不存在冲突。

Input: 

```
tccli vpc CheckAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-12345678 \
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

