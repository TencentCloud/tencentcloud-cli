**Example 1: 查询基础网络互通列表**

查询基础网络互通列表

Input: 

```
tccli vpc DescribeClassicLinkInstances --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-gjui0b5t \
    --Filters.1.Name vm-ip \
    --Filters.1.Values 10.9.0.3.0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "ClassicLinkInstanceSet": [
            {
                "VpcId": "vpc-gjui0b5t",
                "InstanceId": "ins-0x5msjda"
            }
        ],
        "TotalCount": 1
    }
}
```

