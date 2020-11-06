**Example 1: Updating the information of a permission group**



Input: 

```
tccli cfs UpdateCfsPGroup --cli-unfold-argument  \
    --PGroupId pgroup-12345 \
    --Name test \
    --DescInfo test
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

