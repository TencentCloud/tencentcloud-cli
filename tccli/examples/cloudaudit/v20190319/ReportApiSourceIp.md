**Example 1: 异步上报IP**



Input: 

```
tccli cloudaudit ReportApiSourceIp --cli-unfold-argument  \
    --RequestAccountId 100004293724 \
    --RequestSubAccountId 100004293724 \
    --ServiceType cam \
    --ServiceAction DescribeSubAccounts \
    --ServiceRequestId 097e67d8-69b8-48ea-96da-88ba9d9f99e8 \
    --RequestEventTime 1758185552 \
    --SourceIp 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "ad3eb51f-0623-437c-b66f-a971d2678b59"
    }
}
```

