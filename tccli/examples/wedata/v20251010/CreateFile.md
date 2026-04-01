**Example 1: demo**



Input: 

```
tccli wedata CreateFile --cli-unfold-argument  \
    --WorkspaceId 17623335490472931 \
    --ParentMeta.FileId 799995146495934464 \
    --Meta.FileName test_folder \
    --Meta.FileType FOLDER
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileId": "807558146109554688"
        },
        "RequestId": "e64e2ec2-259d-41a0-af2b-5bd6e5b1b788"
    }
}
```

