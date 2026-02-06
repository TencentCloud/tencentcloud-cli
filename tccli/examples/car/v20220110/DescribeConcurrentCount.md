**Example 1: DescribeConcurrentCount示例**



Input: 

```
tccli car DescribeConcurrentCount --cli-unfold-argument  \
    --ProjectId cap-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022",
        "Total": 10,
        "Running": 6
    }
}
```

