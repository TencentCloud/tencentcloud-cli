**Example 1: Querying the real-time recording callback address**

This example shows how to query the real-time recording callback address.

Input: 

```
tccli tiw DescribeOnlineRecordCallback --cli-unfold-argument  \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Callback": "https://example.com/online/callback",
        "CallbackKey": "6vg9G7Fd",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

