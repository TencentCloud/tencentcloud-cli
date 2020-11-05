**Example 1: Request sample**



Input: 

```
tccli redis DescribeInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-5a4py64p\
    --Limit 10\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "InstanceId": "crs-fdjfkldf",
                "AccountName": "test",
                "Remark": "test",
                "Privilege": "rw",
                "ReadonlyPolicy": [
                    "master"
                ],
                "Status": 2
            }
        ],
        "TotalCount": 1,
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db"
    }
}
```

