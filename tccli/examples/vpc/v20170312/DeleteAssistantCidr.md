**Example 1: Deletes secondary CIDR blocks**



Input: 

```
tccli vpc DeleteAssistantCidr --cli-unfold-argument  \
    --Version 2017-03-12 \
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

