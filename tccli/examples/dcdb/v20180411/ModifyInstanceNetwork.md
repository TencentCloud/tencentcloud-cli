**Example 1: 无**



Input: 

```
tccli dcdb ModifyInstanceNetwork --cli-unfold-argument  \
    --InstanceId tdsqlshard-jv8z8fhl \
    --VpcId vpc-xxxxxx \
    --SubnetId subnet-xxxxx \
    --VipReleaseDelay 168
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "FlowId": 1122
    }
}
```

