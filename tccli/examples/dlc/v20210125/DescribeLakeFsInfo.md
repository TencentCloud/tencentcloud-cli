**Example 1: 示例一**



Input: 

```
tccli dlc DescribeLakeFsInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "123-456",
        "LakeFsInfos": [
            {
                "Name": "my-bkt",
                "Type": "chdfs",
                "SpaceUsedSize": "1024",
                "CreateTimeStamp": "1"
            }
        ]
    }
}
```

