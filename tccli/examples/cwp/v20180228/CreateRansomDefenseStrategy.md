**Example 1: 创建或修改防勒索策略**



Input: 

```
tccli cwp CreateRansomDefenseStrategy --cli-unfold-argument  \
    --Status 1 \
    --ExcludeDir /tmp;/var/log \
    --Description 策略备注 \
    --Hour 00:00;11:00;15:00 \
    --BackupType 1 \
    --IncludeDir /root;/data \
    --Weekday 1;2;3 \
    --IsAll 1 \
    --Id 1 \
    --SaveDay 1 \
    --Name ada_api****
```

Output: 
```
{
    "Response": {
        "RequestId": "1703764f-b3ea-4d7f-99cb-cc3a6a62e2ec"
    }
}
```

