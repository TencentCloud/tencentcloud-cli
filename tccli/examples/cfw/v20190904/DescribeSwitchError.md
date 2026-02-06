**Example 1: 互联网边界防火墙开关横幅错误信息**

互联网边界防火墙开关横幅错误信息

Input: 

```
tccli cfw DescribeSwitchError --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ErrIns": "118.24.220.13",
                "ErrKey": "ERR_ENDPOINT_SUBNET",
                "ErrMsg": "1个防火墙开关开启失败(118.24.220.13)，原因：需要指定引流子网和引流内网IP，请尝试逐个手动开启",
                "InsertTime": "2023-07-27 18:07:17"
            }
        ],
        "RequestId": "5f8b7455-6a61-40d6-94a9-d98e9d2f577f"
    }
}
```

