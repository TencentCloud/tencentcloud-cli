**Example 1: ModifyOriginStreamInfo**



Input: 

```
tccli live ModifyOriginStreamInfo --cli-unfold-argument  \
    --DomainName www.test.live \
    --OriginStreamPlayType hls \
    --CdnStreamPlayType hls \
    --OriginStreamType 1 \
    --OriginAddress 81.68.241.194:8082 \
    --OriginAddressType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "2b73d79c-2726-4906-810c-7ad2f2c6f76e"
    }
}
```

