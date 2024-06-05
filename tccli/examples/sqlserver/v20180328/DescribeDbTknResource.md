**Example 1: DescribeDbTknResource**



Input: 

```
tccli sqlserver DescribeDbTknResource --cli-unfold-argument  \
    --ResourceAccount abc \
    --UserResourceId abc \
    --ResourceRegion abc \
    --InstanceType abc \
    --AccountHost abc
```

Output: 
```
{
    "Response": {
        "EnabledRotate": true,
        "ResourceStatus": "abc",
        "AccountStatus": "abc",
        "RequestId": "abc"
    }
}
```

