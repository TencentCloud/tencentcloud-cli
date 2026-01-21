**Example 1: 测试一**



Input: 

```
tccli lcic CreateGroupLiveCodes --cli-unfold-argument  \
    --SdkAppId 3520471 \
    --RoomId 368829238 \
    --Number 3
```

Output: 
```
{
    "Response": {
        "GroupLiveCodes": [
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel1250",
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel125g",
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel1260"
        ],
        "RequestId": "0051e1ca-fb08-4a42-a3e4-7dd6a3ec1681"
    }
}
```

