**Example 1: DescribeSpec**



Input: 

```
tccli tchousex DescribeSpec --cli-unfold-argument  \
    --InstanceType abc
```

Output: 
```
{
    "Response": {
        "Specs": [
            {
                "Id": 0,
                "Type": 0,
                "Name": "abc",
                "Desc": "abc",
                "Cpu": 0,
                "Memory": 0,
                "MinStorage": 0,
                "MaxStorage": 0,
                "BillingParam": "abc",
                "Disabled": true
            }
        ],
        "ErrorMsg": "abc",
        "SparkSpecMaps": [
            {
                "ID": 0,
                "Type": "abc",
                "Name": "abc",
                "Desc": "abc",
                "Cpu": 0,
                "Disabled": true
            }
        ],
        "RequestId": "abc"
    }
}
```

