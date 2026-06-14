**Example 1: DescribeGlossaryEntries**



Input: 

```
tccli tokenhub DescribeGlossaryEntries --cli-unfold-argument  \
    --GlossaryId c5a3fa588af94ddaa50ca896ae6392e5
```

Output: 
```
{
    "Response": {
        "Entries": [
            {
                "EntryId": "b395853160e117177041f0dff7a56274",
                "SourceTerm": "云服务器222",
                "TargetTerm": "Cloud Server222",
                "UpdatedAt": 1779970384
            },
            {
                "EntryId": "bfbc15bbefa2dfcec068372c774ef45c",
                "SourceTerm": "云服务器",
                "TargetTerm": "Cloud Server",
                "UpdatedAt": 1779970384
            }
        ],
        "Page": 1,
        "PageSize": 20,
        "RequestId": "b32c2fcf-bbcc-40a0-8b6c-6af9a4e8a967",
        "Total": 2
    }
}
```

