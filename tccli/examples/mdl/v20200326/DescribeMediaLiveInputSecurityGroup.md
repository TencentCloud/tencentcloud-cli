**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveInputSecurityGroup --cli-unfold-argument  \
    --Id 1111
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": "1111",
            "Name": "xxxx",
            "Whitelist": [
                "0.0.0.0/0"
            ],
            "OccupiedInputs": [
                "xxxx"
            ]
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

