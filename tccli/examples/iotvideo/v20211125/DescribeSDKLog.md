**Example 1: 获取设备上报的日志**



Input: 

```
tccli iotvideo DescribeSDKLog --cli-unfold-argument  \
    --MinTime 1591089960000 \
    --MaxTime 1591091819999 \
    --Keywords productid%3ABJQM4UXMKN+devicename%3Adev01 \
    --Context xxx
```

Output: 
```
{
    "Response": {
        "Context": "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAMjxEFjM2eHBiRXhJVGctQWhqdHoxNUxEeWcAAAAAADI8QRYzNnhwYkV4SVRnLUFoanR6MTVMRHlnAAAAAAAyPEMWMzZ4cGJFeElUZy1BaGp0ejE1TER5ZwAAAAAAMjxCFjM2eHBiRXhJVGctQWhqdHoxNUxEeWcAAAAAADI8RRYzNnhwYkV4SVRnLUFoanR6MTVMRHln",
        "Listover": true,
        "RequestId": "f9201fc1-c2fb-42c9-a08d-be971a1d248b",
        "Results": []
    }
}
```

