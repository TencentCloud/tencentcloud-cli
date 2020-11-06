**Example 1: 卡片续费**

为两张卡片续费。

Input: 

```
tccli ic RenewCards --cli-unfold-argument  \
    --Sdkappid 1420003184 \
    --Iccids ["89860619100041768583","89860438011891822968"] \
    --RenewNum 2
```

Output: 
```
{
    "Response": {
        "RequestId": "0a4dae1c-8a44-4f36-bf18-97564c27a29911",
        "Data": {
            "OrderId": [
                "20200630113185",
                "20200630113186"
            ]
        }
    }
}
```

