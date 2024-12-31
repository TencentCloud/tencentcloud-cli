**Example 1: 更新权限组信息**

更新权限组信息

Input: 

```
tccli cfs UpdateCfsPGroup --cli-unfold-argument  \
    --PGroupId pgroup-12345 \
    --DescInfo pgroup-default \
    --Name pgroup-default
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "PGroupId": "pgroup-12345",
        "Name": "pgroup-default",
        "DescInfo": "pgroup-default"
    }
}
```

