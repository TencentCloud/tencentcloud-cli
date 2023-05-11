**Example 1: 删除基础网络互通**

删除基础网络互通

Input: 

```
tccli vpc DetachClassicLinkVpc --cli-unfold-argument  \
    --VpcId vpc-gjui0b5t \
    --InstanceIds ins-0x5msjda
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

