**Example 1: DescribeInstanceDataReservedSpace用法**



Input: 

```
tccli tdmysql DescribeInstanceDataReservedSpace --cli-unfold-argument  \
    --InstanceId tdsql3-51780d0c
```

Output: 
```
{
    "Response": {
        "IsLegacy": false,
        "KernelVersion": "21.6.4.0",
        "ReservedRate": 2,
        "ReservedSpaceGB": 1,
        "UsableSpaceGB": 49,
        "RequestId": "98b162aa-f038-4e06-a4bd-9a93b589fc3c"
    }
}
```

