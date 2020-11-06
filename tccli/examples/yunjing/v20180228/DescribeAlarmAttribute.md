**Example 1: 获取告警设置**

获取告警设置

Input: 

```
tccli yunjing DescribeAlarmAttribute --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Offline": "CLOSE",
        "Malware": "OPEN",
        "NonlocalLogin": "OPEN",
        "CrackSuccess": "OPEN"
    }
}
```

