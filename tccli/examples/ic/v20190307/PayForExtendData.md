**Example 1: 购买套外流量包**



Input: 

```
tccli ic PayForExtendData --cli-unfold-argument  \
    --Iccid xx \
    --ExtentData 1 \
    --Sdkappid 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "OrderIds": [
                "xx"
            ]
        },
        "RequestId": "xx"
    }
}
```

