**Example 1: 查询Pod事件**

查询Pod事件

Input: 

```
tccli camp DescribePodEvents --cli-unfold-argument  \
    --InstanceID abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Filters": [
            {
                "Name": "abc",
                "Values": [
                    "abc"
                ],
                "Query": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

