**Example 1: Sample request**



Input: 

```
tccli mdp ModifyMediaPackageChannelEndpoint --cli-unfold-argument  \
    --Id XXX \
    --Url XXX \
    --Name XXX \
    --AuthInfo.WhiteIpList 0.0.0.0/0 \
    --AuthInfo.BlackIpList 0.0.0.0/0 \
    --AuthInfo.AuthKey XXX
```

Output: 
```
{
    "Response": {
        "RequestId": "11-222-333"
    }
}
```

