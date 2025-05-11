**Example 1: 查询CVM环境下的实例归属**

查询CVM环境下的实例归属

Input: 

```
tccli sqlserver DescribeInstanceByIp --cli-unfold-argument  \
    --Ip 192.168.0.23 \
    --Env cvm \
    --Port 1433
```

Output: 
```
{
    "Response": {
        "AppId": "251301403",
        "Equipment": "2",
        "RequestId": "8fa41534-eb60-11ee-8790-525400542aa8",
        "ResourceId": "mssql-72td34zp"
    }
}
```

