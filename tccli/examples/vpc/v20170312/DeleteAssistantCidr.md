**Example 1: 删除辅助CIDR**

删除辅助CIDR

Input: 

```
tccli vpc DeleteAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-12345678 \
    --CidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "2fd3d9b3-42cb-4d80-9e19-d97e978df80b"
    }
}
```

