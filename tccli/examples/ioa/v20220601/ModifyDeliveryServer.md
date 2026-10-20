**Example 1: 示例1**



Input: 

```
tccli ioa ModifyDeliveryServer --cli-unfold-argument  \
    --Data.ID 2395 \
    --Data.Name dfa \
    --Data.Description  \
    --Data.TargetSyslogAddress  \
    --Data.TargetSyslogProtocol tcp \
    --Data.TargetSyslogPort 601 \
    --Data.SyslogFacility  \
    --Data.TargetKafkaAddress 10.0.0.1 \
    --Data.TargetKafkaTopic t \
    --Data.KafkaVersion 2.2.2 \
    --Data.KafkaSaslUserName 11 \
    --Data.KafkaSaslPassword ga***cK34imtGd***+**Vr***Y9YkZE*Wd*e*ea*evMt5p8x*jQ*mn**hLez***f7PZW************Y8SK*gSdF+4s****50xYPXz*n****13nv*s0c7Ydeb*q7mutHTlIq**N***MJ0D*4t+3dM7y**ckF*vn*8*v**x0*qKh*zQKmFX6h*****0e5rz*Nmw*v0*Ad*v6wJl+**S8+Q****E***Ej*+5*n7*QBL4**D7seVO9U*73X*qwO*ru****rsGb*ZWn1I***************1***+gq+N***x*kLCwqJ*Dz6z****6e**It2E60YwfoKWgrdW6nC36lDh*****wUBHe43oSMiHHZIejaU7jDK6wz4mndjH1dF1m7p+aFm+kFqMfVjHprvmp+HcopqlFouf1hZuRP/EHw4j8kVw4L78RayXO3BPr4y6dGIWl2a6Hb1k81hMv3+EqwdJsDQvMlvN//kg07AIaTXQmMngOqRV9cA0zFdBet2TqglsjYDWTVaE6yOhYLM5kqyD/G0//Fz5LLWxKJ9cv9KFeKnlkRP0igd2Efoo9aSHUDCecBowNGYF5oXxkJh+yR/FU85YGMXPQQvO7KJgLoEI+kLW5A7XQrq2SiENL08RqOvezlWVoS8C6zJCKtSPxgfIYkgSwHy/zbZN/iYWOx/s= \
    --Data.TargetHttpTimeout 10 \
    --Data.KafkaSSLEnable False \
    --Data.SSLSkipVerify False \
    --Data.ConnectorGroupId  \
    --Data.Type 2 \
    --Data.TargetHttpUrl 
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": 2395
        },
        "RequestId": "b458bf94-563a-4a69-bc21-5f760e92e1d6"
    }
}
```

