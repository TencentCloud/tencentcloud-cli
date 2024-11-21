**Example 1: 成功分派一批代客给业务员**

成功分派一批代客给业务员

Input: 

```
tccli partners AssignClientsToSales --cli-unfold-argument  \
    --ClientUins 1000002 \
    --SalesUin 2000002 \
    --AssignClientStatus normal \
    --AssignActionType assign
```

Output: 
```
{
    "Response": {
        "RequestId": "da71d659-c1f7-4cc6-9f8d-3ef36b867ffe",
        "FailedUins": [
            "1000002"
        ],
        "SucceedUins": [
            "2000002"
        ]
    }
}
```

