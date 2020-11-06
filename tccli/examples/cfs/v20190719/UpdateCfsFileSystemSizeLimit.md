**Example 1: Updating the capacity limit of a file system**



Input: 

```
tccli cfs UpdateCfsFileSystemSizeLimit --cli-unfold-argument  \
    --FileSystemId cfs-12345 \
    --FsLimit 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81"
    }
}
```

