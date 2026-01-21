**Example 1: DescribeGroupLiveCodes**



Input: 

```
tccli lcic DescribeGroupLiveCodes --cli-unfold-argument  \
    --SdkAppId 3520471 \
    --RoomId 368829238
```

Output: 
```
{
    "Response": {
        "GroupLiveCodes": [
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel1260",
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel125g",
            "@TGS#_368829238@TOPIC#_d5nf8ud2et7qpiel1250"
        ],
        "RequestId": "03b04883-07f9-46ad-a25f-5679e060834c"
    }
}
```

