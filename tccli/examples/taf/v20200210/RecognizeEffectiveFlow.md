**Example 1: RecognizeEffectiveFlow**



Input: 

```
tccli taf RecognizeEffectiveFlow --cli-unfold-argument  \
    --BusinessSecurityData.MsgPhone 13112345678 \
    --BusinessSecurityData.MsgSignature oz5I********************GfVv \
    --BusinessSecurityData.MsgContext qw########wqer \
    --BusinessSecurityData.MsgType 1 \
    --BusinessSecurityData.MsgSubType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "Lable": "1",
                "Score": 10.0
            }
        },
        "RequestId": "a6227506-5f00-43cf-9a4c-66fe931cefc9"
    }
}
```

