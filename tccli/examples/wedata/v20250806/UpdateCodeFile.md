**Example 1: UpdateCodeFile**



Input: 

```
tccli wedata UpdateCodeFile --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --CodeFileId 2bfa8813-344f-4858-a2cc-7a07bd10ac1d
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "CodeFileConfig": null,
            "CodeFileContent": "",
            "CodeFileId": "2bfa8813-344f-4858-a2cc-7a07bd10ac1d",
            "CodeFileName": "testFile-0917-1.ipynb",
            "CreateTime": "2025-09-17 18:51:32",
            "OwnerUin": "100028579606",
            "Path": "/testFile-0917-1.ipynb",
            "ProjectId": "1470547050521227264",
            "UpdateTime": "2025-09-18 18:29:13",
            "UpdateUserUin": "100028579606"
        },
        "RequestId": "7da4bd14-ae7b-4dd7-be5b-ee1f0ee586c1"
    }
}
```

