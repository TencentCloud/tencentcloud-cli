**Example 1: demo**



Input: 

```
tccli wedata DeleteFiles --cli-unfold-argument  \
    --WorkspaceId 17623335490472931 \
    --Metas.0.FileId 807558025640755200 \
    --ForceDelete False
```

Output: 
```
{
    "Response": {
        "Data": {
            "OverallSuccess": true,
            "Results": []
        },
        "RequestId": "b08bfb64-b0ef-4bff-9429-56b6aa7f2fe5"
    }
}
```

