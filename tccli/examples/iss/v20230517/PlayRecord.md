**Example 1: 成功**

 

Input: 

```
tccli iss PlayRecord --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890ab \
    --Start 1685611685 \
    --End 1685611785
```

Output: 
```
{
    "Response": {
        "Data": {
            "Flv": "https://test.com.cn/live/12345678-abcd-efgh-ijkl-1234567890ab@aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee.live.flv?start=1685611685&end=1685611785"
        },
        "RequestId": "ba6d7b2e-7ff0-43b2-9f33-56793eee0de7"
    }
}
```

