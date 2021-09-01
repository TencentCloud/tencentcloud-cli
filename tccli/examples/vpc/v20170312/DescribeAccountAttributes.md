**Example 1: 查询账号网络属性**

只支持VPC

Input: 

```
tccli vpc DescribeAccountAttributes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountAttributeSet": [
            {
                "AttributeName": "supported-platforms",
                "AttributeValues": [
                    "VPC"
                ]
            }
        ],
        "RequestId": "68eb9302-af1c-4d6b-b000-1c7851bef46a"
    }
}
```

