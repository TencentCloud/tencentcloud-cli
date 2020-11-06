**Example 1: Request Sample**



Input: 

```
tccli live DescribeLiveStreamState --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName stream1
```

Output: 
```
{
    "Response": {
        "StreamState": "active",
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

