**Example 1: 示例**



Input: 

```
tccli wedata ListModelFiles --cli-unfold-argument  \
    --RunId 7975bfd7b2e244c08179d8740dacafa5 \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "Files": [],
            "NextPageToken": "",
            "RootURI": "mlflow-artifacts:/1/7975bfd7b2e244c08179d8740dacafa5/artifacts"
        },
        "RequestId": "ef0daed9-219c-4393-987e-c7b21bc82160"
    }
}
```

