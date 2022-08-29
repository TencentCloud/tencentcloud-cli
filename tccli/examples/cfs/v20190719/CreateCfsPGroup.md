**Example 1: 创建权限组**



Input: 

```
tccli cfs CreateCfsPGroup --cli-unfold-argument  \
    --DescInfo test_pgroup_desc \
    --Name test_pgroup
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "PGroupId": "pgroup-12345",
        "Name": "test_pgroup",
        "DescInfo": "test_pgroup_desc",
        "BindCfsNum": 0,
        "CDate": "2019-7-20 10:25:33"
    }
}
```

