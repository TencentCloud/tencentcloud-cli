**Example 1: DescribeInstanceFetchMsg**



Input: 

```
tccli cvd DescribeInstanceFetchMsg --cli-unfold-argument  \
    --InstanceId cdi-a \
    --Force True \
    --DesktopName desk-a \
    --UserId usera
```

Output: 
```
{
    "Response": {
        "ProtocolVersion": "version",
        "FetchStatusTicket": "status",
        "RequestId": "rid",
        "FetchUrl": "url",
        "FetchTicket": "ticket"
    }
}
```

