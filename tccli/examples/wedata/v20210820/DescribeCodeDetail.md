**Example 1: test**



Input: 

```
tccli wedata DescribeCodeDetail --cli-unfold-argument  \
    --Id 20220429142707608 \
    --Name 123qweqwe123 \
    --Type 35
```

Output: 
```
{
    "Response": {
        "Data": {
            "Type": "35",
            "Name": "123qweqwe123",
            "ResourceId": "2fe0e0e3-9e79-49fb-872b-4c6a1abdc335",
            "Region": "beijing",
            "ExtraInfo": "2fe0e0e3-9e79-49fb-872b-4c6a1abdc335",
            "Bucket": "beijing-bucket",
            "RemotePath": "/path/resource",
            "FileExtensionType": "hive",
            "Id": "20220429142707608"
        },
        "RequestId": "2fe0e0e3-9e79-49fb-872b-4c6a1abdc335"
    }
}
```

