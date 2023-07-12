**Example 1: 更新权限组信息**

更新权限组信息

Input: 

```
tccli cfs UpdateCfsPGroup --cli-unfold-argument  \
    --PGroupId pgroup-12345 \
    --DescInfo test \
    --Name test
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "PGroupId": "pgroup-12345",
        "Name": "test",
        "DescInfo": "test"
    }
}
```

