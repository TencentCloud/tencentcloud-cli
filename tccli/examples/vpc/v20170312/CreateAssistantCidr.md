**Example 1: 创建辅助CIDR**

创建辅助CIDR

Input: 

```
tccli vpc CreateAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-12345678 \
    --CidrBlocks 172.16.0.0/24
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

