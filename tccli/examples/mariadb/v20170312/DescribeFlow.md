**Example 1: Querying task flow execution status**



Input: 

```
tccli mariadb DescribeFlow --cli-unfold-argument  \
    --FlowId 3340
```

Output: 
```
{
    "Response": {
        "RequestId": "f63a9e3a-cfe9-4fa3-a690-9671ebdf6bd8",
        "Status": 1
    }
}
```

