**Example 1: EnhanceTaDegree**



Input: 

```
tccli taf EnhanceTaDegree --cli-unfold-argument  \
    --BspData.Seq 13169423425 \
    --BspData.OsType 1 \
    --BspData.ImeiMd5 bfd81ee3ed27ad31c95ca75e21365973 \
    --BspData.AgeFloor 23 \
    --BspData.AgeCeil 30 \
    --BspData.Gender 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "IsCheck": 0,
                "IsMatch": 0
            }
        },
        "RequestId": "d12af039-0a21-4519-ba88-f621b1850720"
    }
}
```

