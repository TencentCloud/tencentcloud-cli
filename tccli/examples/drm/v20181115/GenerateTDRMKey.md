**Example 1: 示例1**

示例

Input: 

```
tccli drm GenerateTDRMKey --cli-unfold-argument  \
    --DrmType NORMALAES \
    --Tracks SD \
    --ContentId jackehan1122 \
    --ContentType LiveVideo
```

Output: 
```
{
    "Response": {
        "ContentId": "streamName",
        "RequestId": "ddbdcd59-7a54-4849-bf9f-ad2de811f7d7",
        "TXEncryptionToken": "xxxxx"
    }
}
```

