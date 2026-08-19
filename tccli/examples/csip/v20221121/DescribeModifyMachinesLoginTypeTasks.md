**Example 1: 成功**



Input: 

```
tccli csip DescribeModifyMachinesLoginTypeTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 1,
                "Status": 1,
                "SuccessCount": 1,
                "FailList": [
                    {
                        "MachineName": "test-ins",
                        "InstanceId": "ins-fjif18fja",
                        "MachineIp": "10.0.0.*",
                        "MachineWanIp": "",
                        "Region": "ap-guangzhou",
                        "MachineType": "CVM",
                        "Message": ""
                    }
                ]
            }
        ],
        "RequestId": "51faba98-f124-4f72-85**-d41bca64e1a7"
    }
}
```

