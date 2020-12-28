**Example 1: 删除安全组规则**



Input: 

```
tccli cfw DeleteSecurityGroupRule --cli-unfold-argument  \
    --Id 1 \
    --Area ap-guangzhou \
    --Direction 0 \
    --IsDelReverse 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Info": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

