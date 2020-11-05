**Example 1: Sample request**

This example shows you how to pause the stream pushed by a host.

Input: 

```
tccli live DropLiveStream --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com\
    --AppName live\
    --StreamName stream1
```

Output: 
```
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

