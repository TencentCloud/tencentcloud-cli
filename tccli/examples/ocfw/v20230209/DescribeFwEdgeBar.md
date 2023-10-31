**Example 1: 互联网边界页概览数据**

互联网边界页概览数据

Input: 

```
tccli ocfw DescribeFwEdgeBar --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InFlowMax": 1000000,
        "OutFlowMax": 2000000,
        "Width": 100,
        "SerialWidth": 50,
        "UnUsedWidth": 50,
        "NatWidth": 50,
        "AutoDefence": 1,
        "OpenSwitchNum": 10,
        "SwitchQuota": 20,
        "SerialRegionNum": "1",
        "InstanceQuota": 10,
        "CloseSwitchNum": 10,
        "RequestId": "abc"
    }
}
```

