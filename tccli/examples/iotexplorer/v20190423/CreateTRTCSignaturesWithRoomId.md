**Example 1: 成功示例 **



Input: 

```
tccli iotexplorer CreateTRTCSignaturesWithRoomId --cli-unfold-argument  \
    --TRTCUserIds test1 \
    --RoomId test
```

Output: 
```
{
    "Response": {
        "RequestId": "keyixie_38bc26eb-89c5-4e7c-bdb3-9a4fe25e719f",
        "TRTCParamList": [
            {
                "SdkAppId": 111111,
                "UserId": "test1",
                "UserSig": "eJwszcvOgjAQBe123213131321313QRN5AbRVR6U2dIK3*O4mwPY7Oed8oF7vEvcM1DkweaYR-wci6zzTkVwHBthFFjAG0V6bEMiCERpR1232132132133xio-CtUdsOqx*WlYb8-z95-BcsYtyVa2RYrcbjd6adadsadsadvmo-XAtE4TvLwAA--*MzTGH",
                "StrRoomId": "gl-40badb65asdsadasdsad40b2192f948845",
                "PrivateKey": "eJw0j19PszAUxr-LuX3fjFJahk12UaxUzVplwha4c2nHCtlC*KPbjN-dOObv8ndynjzPF2TLt5k9ta6zwKKQIPT-qpyxx8HtnO2AwWD7wYfp0JvmvW2dAeYThAgJg7vbS*8qYNALlMdbj*5THev546k4yvu5RkRG-0wbea-Pm2rs6mVdoABT3li5PpiRJLZFcb8F5loRwvOufD4RFfiz0GL2BWbldN17peHgqrLAyrleq*xwkrkROMUKfl0VllzLusGvYgK6XTxV*XjuhfPEHz-BAAA--9iV1Mr"
            }
        ]
    }
}
```

