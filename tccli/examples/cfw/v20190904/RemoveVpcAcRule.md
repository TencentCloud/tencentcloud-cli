**Example 1: 删除VPC间规则**



Input: 

```
tccli cfw RemoveVpcAcRule --cli-unfold-argument  \
    --RuleUuids 8888 8889
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            8888,
            8889
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

