**Example 1: 创建文件记录**



Input: 

```
tccli rum CreateReleaseFile --cli-unfold-argument  \
    --ProjectID 1 \
    --Files.0.Version '0.0.1' \
    --Files.0.FileName 'a.js.map' \
    --Files.0.FileKey '1-0.0.1-a.js.map' \
    --Files.0.FileHash 'sadfjfhdkhfksdjhg;'
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

