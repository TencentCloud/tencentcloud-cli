**Example 1: 列出命名空间列表**

列出命名空间列表

Input: 

```
tccli scf ListNamespaces --cli-unfold-argument  \
    --SearchKey.0.Key Namespace \
    --SearchKey.0.Value ns1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Namespaces": [
            {
                "Name": "ns1",
                "Description": "",
                "AddTime": "2024-12-17 15:28:55",
                "ModTime": "2024-12-17 15:28:55",
                "Type": "default",
                "Stamp": "default",
                "Status": "Active",
                "StatusReason": null,
                "ResourceEnv": null
            },
            {
                "Name": "default",
                "Description": "",
                "AddTime": "2024-10-17 09:29:45",
                "ModTime": "2024-10-17 09:29:45",
                "Type": "default",
                "Stamp": "default",
                "Status": "Active",
                "StatusReason": null,
                "ResourceEnv": null
            }
        ],
        "RequestId": "sdfsdfs-3de5-459c-984a-cb43ec2625d2"
    }
}
```

