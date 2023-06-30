**Example 1: DescribeAuthDomains**

DescribeAuthDomains 

Input: 

```
tccli tcb DescribeAuthDomains --cli-unfold-argument  \
    --EnvId test-23
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "Domains": [
            {
                "Status": "ENABLE",
                "Domain": "localhost",
                "UpdateTime": "2020-03-02 17:16:39",
                "CreateTime": "2020-03-02 17:16:39",
                "Type": "USER",
                "Id": "38e5c159-c715-4887-9a15-453e6749e949"
            }
        ]
    }
}
```

