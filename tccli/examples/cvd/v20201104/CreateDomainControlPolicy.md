**Example 1: CreateDomainControlPolicy**



Input: 

```
tccli cvd CreateDomainControlPolicy --cli-unfold-argument  \
    --Name test-policy \
    --Description test policy \
    --Type WHITE \
    --DetailSet.0.Domain *.testcvd.com \
    --DetailSet.0.Address 10.0.10.12 \
    --DetailSet.0.Description test domain \
    --InstanceIds cdi-r4j5k6ras6zgtrw
```

Output: 
```
{
    "Response": {
        "PolicyId": "domain-wd8d7hdy",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

