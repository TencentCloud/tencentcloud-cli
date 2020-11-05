**Example 1: Deleting a permission group rule**



Input: 

```
tccli cfs DeleteCfsRule --cli-unfold-argument  \
    --PGroupId pgroup-12345\
    --RuleId rule-12345
```

Output: 
```
{
    "Response": {
        "PGroupId": "pgroup-12345",
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "RuleId": "rule-12345"
    }
}
```

