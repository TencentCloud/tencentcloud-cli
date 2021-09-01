**Example 1: CreateExternalAnchor**



Input: 

```
tccli cpdp CreateExternalAnchor --cli-unfold-argument  \
    --IdCardFront xx \
    --IdNo xx \
    --IdCardReverse xx \
    --Uid xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "AnchorId": "xx"
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

