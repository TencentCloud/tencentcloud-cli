**Example 1: 获取共享空间**



Input: 

```
tccli cme DescribeSharedSpace --cli-unfold-argument  \
    --Operator user_id_d1c5eb0ee4994419b465 \
    --Platform test \
    --Authorizee.Type TEAM \
    --Authorizee.Id cmetid_acc5ddee49933d2b4338ud8d9
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AuthorizerSet": [
            {
                "Type": "PERSON",
                "Id": "user_id_d1c5eb0ee4994419b465"
            }
        ],
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb6c9"
    }
}
```

