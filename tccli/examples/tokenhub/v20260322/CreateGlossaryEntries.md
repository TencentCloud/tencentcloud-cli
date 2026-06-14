**Example 1: CreateGlossaryEntries**



Input: 

```
tccli tokenhub CreateGlossaryEntries --cli-unfold-argument  \
    --GlossaryId c5a3fa588af94ddaa50ca896ae6392e5 \
    --Entries.0.SourceTerm 云服务器 \
    --Entries.0.TargetTerm Cloud Server \
    --Entries.1.SourceTerm 云服务器222 \
    --Entries.1.TargetTerm Cloud Server222
```

Output: 
```
{
    "Response": {
        "Entries": [
            {
                "EntryId": "bfbc15bbefa2dfcec068372c774ef45c",
                "SourceTerm": "云服务器",
                "TargetTerm": "Cloud Server",
                "UpdatedAt": 1779970384
            },
            {
                "EntryId": "b395853160e117177041f0dff7a56274",
                "SourceTerm": "云服务器222",
                "TargetTerm": "Cloud Server222",
                "UpdatedAt": 1779970384
            }
        ],
        "RequestId": "04cfa4f3-68d1-4a85-9ae3-3e2bd6d46fbb"
    }
}
```

