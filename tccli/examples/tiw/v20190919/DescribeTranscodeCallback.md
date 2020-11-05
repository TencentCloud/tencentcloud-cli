**Example 1: Querying the document transcoding callback address**

This example shows how to query the document transcoding callback address.

Input: 

```
tccli tiw DescribeTranscodeCallback --cli-unfold-argument  \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Callback": "https://example.com/transcode/callback",
        "CallbackKey": "6vg9G7Fd",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

