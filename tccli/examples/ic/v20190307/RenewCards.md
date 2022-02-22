**Example 1: 卡片续费**

为两张卡片续费。

Input: 

```
tccli ic RenewCards --cli-unfold-argument  \
    --Iccids 89314304010606595418 \
    --Sdkappid 1 \
    --RenewNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0a4dae1c-8a44-4f36-bf18-97564c27a29911",
        "Data": {}
    }
}
```

