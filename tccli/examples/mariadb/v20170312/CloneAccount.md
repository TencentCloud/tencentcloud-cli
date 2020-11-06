**Example 1: Cloning an existing account**



Input: 

```
tccli mariadb CloneAccount --cli-unfold-argument  \
    --InstanceId tdsql-6a0lwzzj \
    --SrcUser testuser \
    --SrcHost 10.10.10.% \
    --DstUser testuser \
    --DstHost 10.10.20.% \
    --DstDesc testclone
```

Output: 
```
{
    "Response": {
        "RequestId": "dc521928-4651-44ac-81f0-7c8acdd8b73e",
        "FlowId": 4123
    }
}
```

