**Example 1: 示例**



Input: 

```
tccli mqtt DescribeBlockRuleList --cli-unfold-argument  \
    --InstanceId mqtt-3ja5wo5b
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": 1774597726000,
                "ExpireTime": 1774597703556,
                "Include": "client*",
                "Name": "cleint",
                "Remark": "this is remark",
                "Type": 1,
                "UpdateTime": 1774597726000
            }
        ],
        "TotalCount": 3,
        "RequestId": "b5cf470b-e1d9-49de-9e30-3988cb8a68dd"
    }
}
```

