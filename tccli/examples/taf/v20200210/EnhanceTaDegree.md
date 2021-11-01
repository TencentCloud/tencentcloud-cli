**Example 1: EnhanceTaDegree**



Input: 

```
tccli taf EnhanceTaDegree --cli-unfold-argument  \
    --BspData.Seq 1235467 \
    --BspData.OsType 1 \
    --BspData.AgeFloor 20 \
    --BspData.AgeCeil 30 \
    --BspData.Gender 2 \
    --BspData.Imei 86xxxxxxxxxxxx
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

