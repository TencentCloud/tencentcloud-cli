**Example 1: Querying the network attributes of an account**

This example only supports VPC.

Input: 

```
tccli vpc DescribeAccountAttributes --cli-unfold-argument  \
    --Version 2017-03-12
```

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

