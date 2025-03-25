**Example 1: ScaleOutInstance**



Input: 

```
tccli cdwpg ScaleOutInstance --cli-unfold-argument  \
    --InstanceId cdwpg-abcxxxxx \
    --NodeType dn \
    --ScaleOutCount 2
```

Output: 
```
{
    "Response": {
        "FlowId": "1324",
        "ErrorMsg": "",
        "RequestId": "abcds-xxxss"
    }
}
```

