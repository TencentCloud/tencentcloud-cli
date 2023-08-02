**Example 1: 成功**

 

Input: 

```
tccli iss DescribeDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {}
}
```

**Example 2: 设备不存在**

 

Input: 

```
tccli iss DescribeDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {}
}
```

