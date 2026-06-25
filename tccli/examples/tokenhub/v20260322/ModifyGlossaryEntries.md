**Example 1: ModifyGlossaryEntries**



Input: 

```
tccli tokenhub ModifyGlossaryEntries --cli-unfold-argument  \
    --GlossaryId c5a3fa588af94ddaa50ca896ae6392e5 \
    --Entries.0.EntryId bfbc15bbefa2dfcec068372c774ef45c \
    --Entries.0.SourceTerm 云服务器-修改后 \
    --Entries.0.TargetTerm Cloud Server-new
```

Output: 
```
{
    "Response": {
        "Entries": [
            {
                "EntryId": "bfbc15bbefa2dfcec068372c774ef45c",
                "SourceTerm": "云服务器-修改后",
                "TargetTerm": "Cloud Server-new",
                "UpdatedAt": 1780024696
            }
        ],
        "RequestId": "1ed04a04-e786-43eb-a7c4-4b14ea4abd1d"
    }
}
```

