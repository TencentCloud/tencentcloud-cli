**Example 1: 按具体规则 ID 删除一条 VPC 间规则**

按具体规则 ID 删除一条 VPC 间规则。

Input: 

```
tccli cfw RemoveVpcAcRule --cli-unfold-argument  \
    --RuleUuids 9001001
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            9001001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

