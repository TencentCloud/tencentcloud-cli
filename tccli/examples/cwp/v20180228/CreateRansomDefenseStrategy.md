**Example 1: 创建或修改防勒索策略**



Input: 

```
tccli cwp CreateRansomDefenseStrategy --cli-unfold-argument  \
    --Status 1 \
    --ExcludeDir xx \
    --Description xx \
    --Hour xx \
    --BackupType 1 \
    --IncludeDir xx \
    --Weekday xx \
    --IsAll 1 \
    --Id 1 \
    --SaveDay 1 \
    --Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

