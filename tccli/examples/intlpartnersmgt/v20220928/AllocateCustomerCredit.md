**Example 1: 设置客户信用额度**



Input: 

```
tccli intlpartnersmgt AllocateCustomerCredit --cli-unfold-argument  \
    --ClientUin 1 \
    --AddedCredit 10
```

Output: 
```
{
    "Response": {
        "RemainingCredit": 100,
        "RequestId": "2b7c676e-bb4b-449d-89e6-4866132036c5",
        "TotalCredit": 100
    }
}
```

