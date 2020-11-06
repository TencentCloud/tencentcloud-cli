**Example 1: Cloning an existing account**



Input: 

```
tccli dcdb CloneAccount --cli-unfold-argument  \
    --InstanceId dcdbt-ovulpcjf \
    --SrcUser testuser1 \
    --SrcHost 172.17.% \
    --DstUser testuser1 \
    --DstHost 172.20.% \
    --DstDesc testclone
```

Output: 
```
{
    "Response": {
        "RequestId": "8875137e-4ce2-43cb-a0ab-704b775790d1",
        "FlowId": 4127
    }
}
```

